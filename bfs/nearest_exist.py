from collections import deque

class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        rows, cols = len(maze), len(maze[0])
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        # Marking the entrance as 'visited'
        start_row, start_col = entrance
        maze[start_row][start_col] = "+"

        # Start BFS at the entrance
        queue = deque()
        queue.append([start_row, start_col, 0])

        while queue:
            curr_row, curr_col, curr_distance = queue.popleft()
            # check all 4 neighbor cells if they are an empty cell
            for d in directions:
                next_row = curr_row + d[0]
                next_col = curr_col + d[1]

                # check for any 'unvisited' 'empty' neighbors
                if rows > next_row >= 0 and cols > next_col >= 0 and maze[next_row][next_col] == ".":
                    # if this empty cell is an 'exit'
                    if next_row == 0 or next_row == rows - 1 or next_col == 0 or next_col == cols - 1:
                        return curr_distance + 1

                    # if it's not add it to the visited queue
                    maze[next_row][next_col] = "+"
                    queue.append([next_row, next_col, curr_distance + 1])

        # if no exits at the end
        return -1
