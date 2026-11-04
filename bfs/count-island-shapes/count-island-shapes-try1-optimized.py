from collections import deque
from typing import List

# LeetCode 694: Number of Distinct Islands
# Time: O(m * n). Space: O(m * n) worst case (queue + stored shapes).
# Lines marked CHANGE are the optimizations to the original solution.


def count_distinct_islands(grid: List[List[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    shapes = set()

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != 1:
                continue

            # CHANGE 1 (memory): flip visited land to 0 instead of using a
            # `seen` set. Saves the O(m * n) set.
            # Ask first: this destroys the caller's grid.
            grid[r][c] = 0
            q = deque([(r, c)])
            cells = []

            while q:
                cr, cc = q.popleft()
                cells.append((cr - r, cc - c))  # offset from this island's anchor
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = cr + dr, cc + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 0  # mark on enqueue so no cell is queued twice
                        q.append((nr, nc))

            # CHANGE 2 (memory): store one int per shape, not the whole set.
            # Tradeoff: a hash collision could undercount. Very unlikely with
            # at most 1,250 islands in a 50x50 grid.
            shapes.add(hash(frozenset(cells)))

    return len(shapes)


# Talk through, don't code (if asked "what if this runs millions of times?"):
# 1. Do the math: 10M calls x 2,500 cells is too much for one core.
# 2. Same grid repeated: cache the answer, keyed on a grid ID or version.
# 3. Grid changes one cell at a time: update incrementally with Union Find
#    instead of rescanning everything.


if __name__ == "__main__":
    assert count_distinct_islands([[1, 1, 0, 1, 1], [1, 0, 0, 1, 0]]) == 1
    assert count_distinct_islands([[1, 1, 0, 0], [0, 0, 0, 1], [0, 0, 0, 1]]) == 2
    print("All tests passed.")