from collections import deque

class Solution:
    def numDistinctIslands(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        shapes = set()

        def bfs(r, c):
            # mark initial as visited, this is also the origin
            grid[r][c] = 0
            q = deque([(r, c)])
            cells = []

            while q:
                cr, cc = q.popleft()
                # subtracting by origin so we handle translations
                cells.append(((cr - r), (cc - c)))
                for dr, dc in directions:
                    nr, nc = dr + cr, dc + cc
                    if (0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1):
                        q.append((nr, nc))
                        # changing in place, so we handle the visited and don't create a infinite loop
                        grid[nr][nc] = 0
            return cells

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    # implement bfs and add result to shapes
                    shapes.add(tuple(bfs(r,c)))

        return len(shapes)