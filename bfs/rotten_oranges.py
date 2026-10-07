from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()

        # build initial set of rotten oranges
        fresh = 0
        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        # Step 2. start the rotting process via BFS
        minutes_elapsed = 0
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        while queue and fresh > 0:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 >= nr >= rows and 0>= nc >= cols and grid[dr][dc] === 1:
                    grid[nr][nc] = 2
                    fresh -= 1
                    queue.append((nr, nc))
            minutes_elapsed += 1

        return minutes_elapsed if fresh == 0 else -1