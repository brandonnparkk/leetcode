from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # you're looking at a 'connected components' problem
        # you use BFS to handle this. When using bfs, you should be using a queue, fifo
        # we have to look at the the different directions (up, down, left, right)

        # time complexity: o(n) because we go through each item in the list once
        # space complexity: o(n) because we store the values in a list
        
        # 1. ask questions. what are some questions you may have?
        # will every item be either a '0' or '1'?
        # how big of a grid this be?

        # 2. walk through the logic
        rows, cols = len(grid), len(grid[0])
        count = 0
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        # build the queue based on the current grid
        for r in range(rows):
            for c in range(cols):
                # this is an island
                if grid[r][c] == '1':
                    count += 1
                    # reassign the value of the 1 to 0.
                    grid[r][c] = '0'
                    # add the row,col combo to the queue
                    q = deque([(r, c)])
                    while q:
                        # pop the first item off the queue to get the current row and current col
                        cr, cc = q.popleft()
                        # loop through the 4 directions
                        for dr, dc in directions:
                            nr, nc = cr + dr, cc + dc
                            #  make sure you check for islands, but stay in the grid bounds
                            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
                                # re-assign to 0, when queued not when popped
                                grid[nr][nc] = '0'
                                # add this row,col combo to the queue, so you look through the 4 directions for this new location
                                q.append((nr, nc))
        return count