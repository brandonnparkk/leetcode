from collections import deque

def oranges_rotting(grid: list[list[int]]) -> int:
    pass
    # clarifying questions
    # how big can the grid parameter be? 
    # am I able to mutate the grid parameter?
    # how big can the output be?

    # reason why I ask about how big, is this will dictate if I need to use an iterative dfs
    # if we go that way, because of python's stack overflow issue

    # reason why I am asking if we can mutate the grid, it will allow us to save space on memory instead of having to create a variable each time.

    # idea to implement
    # grid traversal - bfs is good for this kind of functionality
    # so with bfs, we'll be using a queue

    # create variable for minutes_elapsed set to 0
    # looping through the items in the grid
        # check if item is a rotten orange, then reassign it to 0
            # add this row, col to the queue
        # while there's things in the queue
            # get the first item and if rotten, check in all 4 directions, it'll take the row, col and the minutes_elapsed
            # check if the value at that coordinate is 1, if it is, you'll update that value to be 2
            # if value is 0, don't do anything
        # after bfs is done, increment minutes
        # after the loop is done, but there are still fresh oranges, then return -1
            # otherwise return minutes_elapsed

    # implementation
    minutes_elapsed = 0
    num_fresh = 0
    q = deque()
    rows, cols = len(grid), len(grid[0])
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    for row in range(rows):
        for col in range(cols):
            # definitely thinking there's something to do with fresh oranges that we need to check
            if grid[row][col] == 1:
                num_fresh += 1
            if grid[row][col] == 2:
                q.append((row, col))
    
    while q and num_fresh > 0:
        cr, cc = q.popleft()
        for dr, dc in directions:
            nr, nc = cr + dr, cc + dc
            if (0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1):
                grid[nr][nc] = 2
                num_fresh -= 1
                q.append((nr, nc))
        minutes_elapsed += 1
    
    return minutes_elapsed if num_fresh == 0 else -1