from collections import deque

class Solution:
    def numDistinctIslands(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        shapes = set()
        directions = [(0, 1), (-1, 0), (1, 0), (0, -1)]

        def bfs(r,c):
            grid[r][c] = 0
            q = deque([(r,c)])
            cells = []

            while q:
                cr, cc = q.popleft()
                cells.append((cr - r, cc - c))
                for dr, dc in directions:
                    nr, nc = dr + cr, dc + cc
                    if 0 <= cr < rows and 0 <= cc < cols and grid[cr][cc] == 1:
                        grid[nr][nc] = 0
                        q.append((nr, nc))
            return tuple(cells)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    shapes.add(bfs(r,c))
        return len(shapes)