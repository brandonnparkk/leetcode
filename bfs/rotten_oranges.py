from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()

        # build initial set of rotten oranges
        fresh_oranges = 0
        ROWS, COLS = len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_oranges += 1
        
        # mark the round / level
        queue.append((-1, -1))

        # Step 2. start the rotting process via BFS
        minutes_elapsed = -1
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        while queue:
            row, col = queue.popleft()
            if row == -1:
                # if the queue has no rotten oranges,
                # we need to output -1
                minutes_elapsed += 1
                # avoid endless loop
                if queue:
                    queue.append((-1, -1))
            else:
                # this is a rotten orange
                for d in directions:
                    # row is d[0] = left
                    # col is d[1] = right
                    neighbor_row, neighbor_col = row + d[0], col + d[1]
                    if ROWS > neighbor_row >= 0 and COLS > neighbor_col >= 0:
                        if grid[neighbor_row][neighbor_col] == 1:
                            # this orange would become rotten
                            grid[neighbor_row][neighbor_col] = 2
                            fresh_oranges -= 1
                            # this is now a rotten orange, add it to the queue
                            queue.append((neighbor_row, neighbor_col))
        
        # if no fresh oranges, return minutes elapsed.
        # otherwise, return -1
        return minutes_elapsed if fresh_oranges == 0 else -1
