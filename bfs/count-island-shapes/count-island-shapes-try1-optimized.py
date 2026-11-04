"""
Count Island Shapes Up to Translation Only (LeetCode 694: Number of Distinct Islands)

Core idea:
    1. Find each island with BFS.
    2. Convert it to a canonical form: offsets from the island's own anchor.
    3. Put the canonical forms in a set. The answer is the size of the set.

Complexity:
    Time:  O(m * n). Every cell is visited once.
    Space: O(m * n) worst case for the BFS queue and stored shapes.
           Visited tracking costs O(1) extra because we mutate the grid.
"""

from collections import Counter, deque
from typing import Dict, FrozenSet, List, Tuple

Cell = Tuple[int, int]

# 4 directions because only shared edges connect.
# FOLLOW-UP: "What if diagonals connect?" Add the 4 diagonal moves here.
# Nothing else in the solution changes.
DIRS = ((1, 0), (-1, 0), (0, 1), (0, -1))


def _collect_island(grid: List[List[int]], r: int, c: int) -> List[Cell]:
    """BFS from (r, c). Returns the island's absolute cells."""
    rows, cols = len(grid), len(grid[0])

    # OPTIMIZATION (memory): mark visited by flipping land to 0 instead of
    # keeping a separate visited set. Saves the O(m * n) set.
    # Tradeoff: this destroys the caller's grid. Ask the interviewer first.
    # If mutation is not allowed: use a visited set, or pass in a copy.
    grid[r][c] = 0

    # OPTIMIZATION (safety): iterative BFS with a deque, not recursive DFS.
    # Python's default recursion limit is 1000. A snake shaped island in a
    # 50x50 grid can be 2,500 cells long and crash a recursive DFS.
    # deque.popleft() is O(1). list.pop(0) would be O(n).
    q = deque([(r, c)])
    cells = []

    while q:
        cr, cc = q.popleft()
        cells.append((cr, cc))
        for dr, dc in DIRS:
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                # Mark on ENQUEUE, not dequeue, so no cell is queued twice.
                grid[nr][nc] = 0
                q.append((nr, nc))

    return cells


def _translation_key(cells: List[Cell], anchor_r: int, anchor_c: int) -> FrozenSet[Cell]:
    """Canonical form for translation: offsets from the island's own anchor.

    Passes the "slide it one cell" test: moving the island does not change the key.
    The anchor is the first cell found in the top to bottom, left to right scan.
    Offsets can be negative (a lower row can extend left of the anchor). That is fine.
    frozenset is hashable and ignores order, so BFS visit order does not matter.
    """
    return frozenset((cr - anchor_r, cc - anchor_c) for cr, cc in cells)


def count_distinct_islands(grid: List[List[int]]) -> int:
    """Main answer, with the memory optimizations applied."""
    rows, cols = len(grid), len(grid[0])
    shapes = set()

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                cells = _collect_island(grid, r, c)
                key = _translation_key(cells, r, c)

                # OPTIMIZATION (memory): store one int per shape instead of the
                # whole set of coordinates.
                # hash() on tuples of ints is stable in Python. Hash randomization
                # only affects str and bytes.
                # Tradeoff: two different shapes could collide and get counted once.
                # Very unlikely here: a 50x50 grid has at most 1,250 islands
                # (checkerboard), against a 64 bit hash space.
                # Fix if asked: dict of hash -> list of full shapes, and compare the
                # full shapes only when two hashes match.
                shapes.add(hash(key))

    return len(shapes)


def count_each_shape(grid: List[List[int]]) -> Dict[FrozenSet[Cell], int]:
    """FOLLOW-UP: "How many islands of each shape?" Swap the set for a Counter.

    The most common shape is then counts.most_common(1).
    """
    rows, cols = len(grid), len(grid[0])
    counts = Counter()

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                cells = _collect_island(grid, r, c)
                counts[_translation_key(cells, r, c)] += 1

    return counts


def _rotation_reflection_key(cells: List[Cell]) -> Tuple[Cell, ...]:
    """FOLLOW-UP (LeetCode 711): rotations and reflections also count as the same.

    The "first scanned cell" anchor breaks here: after a rotation, a different
    cell comes first. So normalize each version by its min row and min col.

    Steps:
        1. Build all 8 versions: 4 sign flips, each with and without swapping r and c.
        2. Shift each so its smallest row and col are 0, then sort it.
        3. Pick the smallest version. Every equivalent island picks the same one.

    Sorted tuples are used instead of frozensets because min() needs an order.
    """
    versions = []
    for sign_r, sign_c in ((1, 1), (1, -1), (-1, 1), (-1, -1)):
        for swap in (False, True):
            pts = [(sign_r * c, sign_c * r) if swap else (sign_r * r, sign_c * c) for r, c in cells]
            min_r = min(p[0] for p in pts)
            min_c = min(p[1] for p in pts)
            versions.append(tuple(sorted((pr - min_r, pc - min_c) for pr, pc in pts)))
    return min(versions)


def count_distinct_islands_with_rotation(grid: List[List[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    shapes = set()

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                shapes.add(_rotation_reflection_key(_collect_island(grid, r, c)))

    return len(shapes)


if __name__ == "__main__":
    # Copies are passed in because every function mutates the grid.
    ex1 = [[1, 1, 0, 1, 1], [1, 0, 0, 1, 0]]
    ex2 = [[1, 1, 0, 0], [0, 0, 0, 1], [0, 0, 0, 1]]

    assert count_distinct_islands([row[:] for row in ex1]) == 1
    assert count_distinct_islands([row[:] for row in ex2]) == 2

    # Horizontal and vertical pairs become one shape once rotation counts.
    assert count_distinct_islands_with_rotation([row[:] for row in ex2]) == 1

    # Two L shapes that are reflections of each other: distinct under
    # translation only, the same once reflection counts.
    mirrored = [[1, 1, 0, 1, 1], [1, 0, 0, 0, 1]]
    assert count_distinct_islands([row[:] for row in mirrored]) == 2
    assert count_distinct_islands_with_rotation([row[:] for row in mirrored]) == 1

    counts = count_each_shape([row[:] for row in ex1])
    assert list(counts.values()) == [2]

    print("All tests passed.")


# =============================================================================
# TALK THROUGH ONLY: optimizations to explain out loud, not code
# =============================================================================
#
# 1. "Called 10 million times per second"
#    - Do the math first: 10M calls x 2,500 cells = about 2.5 x 10^10 cell
#      visits per second. Not possible on one core. Say that out loud.
#    - Then ask what is actually repeating.
#
# 2. Same grid queried again and again
#    - Cache the answer.
#    - Key the cache on a grid ID or version number, not on a hash of the
#      grid. Hashing the grid is O(m * n), the same cost as solving it.
#
# 3. Grid changes a little between calls (one cell flips to land)
#    - Do not recompute the whole grid. Update incrementally.
#    - Union Find tracks which island each cell belongs to (see LC 305,
#      Number of Islands II).
#    - Keep a Counter of shape_key -> count. Answer = keys with count > 0.
#    - On a merge: decrement the old shapes, rebuild the merged shape,
#      increment the new one.
#    - Be honest about the cost: a merge can be O(island size) because the
#      anchor moves and every offset changes.
#
# 4. Lower constant factors
#    - Each row is 50 columns or fewer, so it fits in one 64 bit int.
#      Bit operations can find land cells and neighbors quickly.
#      (Bigger win in C++ than in Python.)
#    - Many independent grids: process them in parallel. In Python that means
#      multiprocessing, since threads do not speed up CPU bound work under
#      the GIL.
#
# 5. Memory is very limited
#    - Already in the code: mutate the grid, iterative BFS, store hashes.
#    - If mutation is not allowed: a bitset of rows * cols bits
#      (2,500 bits is about 313 bytes) instead of a set of tuples.
#    - Compact shape encoding: a bitmask over the island's bounding box plus
#      its width and height.
#
# 6. Grid is too large to fit in memory (arrives one row at a time)
#    - Streaming connected component labeling: keep two rows in memory and
#      use Union Find to join cells across rows.
#    - Name the hard part: a shape spans many rows, so you have to build each
#      island's cell list as rows arrive and finalize it once no cell in the
#      new row touches it.
#
# 7. Grid is huge but mostly water
#    - Store only the land cells in a set instead of a full 2D array.
#      Memory becomes O(land cells) instead of O(m * n).
# =============================================================================