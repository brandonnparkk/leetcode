from collections import deque

class Solution:
    def minimumKnightMoves(self, x: int, y: int) -> int:
        # Your code goes here
        directions = [
            (2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)]
        # initialize queue
        queue = deque([(0, 0, 0)])
        visited = {(0, 0)}

        # bfs
        while queue:
            cx, cy, moves = queue.popleft()
            if (cx, cy) == (x, y):
                return moves
            for dx, dy in directions:
                nx, ny = dx + cx, dy + cy
                if (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny, moves + 1))

        # if unreachable
        return -1