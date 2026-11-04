from collections import deque

def count_distinct_islands(grid):
    rows, cols = len(grid), len(grid[0])
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    visited = set()
    shapes = set()

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != 1 or (r,c) in visited:
                continue
            visited.add((r,c))
            q = deque([(r,c)])
            # this has the normalized coordinates, we subtract each cell by origin (ex. first cell of island)
            cells = []
            while q:
                cr, cc = q.popleft()
                # subtracts by anchor (first 'island' cell (r,c))
                cells.append((cr - r, cc - c))
                for dr, dc in directions:
                    nr, nc = dr + cr, dc + cc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1 and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        q.append((nr,nc))
            shapes.add(frozenset(cells))
    return shapes