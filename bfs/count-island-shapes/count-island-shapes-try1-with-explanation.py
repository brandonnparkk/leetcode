from collections import deque

def count_distinct_islands(grid):
    rows, cols = len(grid), len(grid[0])
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    visited = set()
    shapes = set()

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != 1 or (r, c) in visited:
                continue
            visited.add((r, c))
            q = deque([(r, c)])
            # offsets from the anchor (first cell of this island)
            cells = []
            while q:
                cr, cc = q.popleft()
                cells.append((cr - r, cc - c))
                for dr, dc in directions:
                    nr, nc = dr + cr, dc + cc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1 and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        q.append((nr, nc))
            # Works because BFS visits every
            # translated copy in the same order (same anchor, same direction order).
            shapes.add(tuple(cells))

    return len(shapes)