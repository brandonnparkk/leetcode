board = [
    ['B', 'L', 'C', 'H'],
    ['D', 'E', 'L', 'T'],
    ['D', 'A', 'K', 'A'],
]
word = "BLEED"

from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # solution is to use a backtracking approach
        # find the target word one char at a time using DFS
        # loop through the grid cell by cell. Then, if any character matches the first letter of our target word
        # we init DFS from that cell

        # create a helper dfs function. it will hold the row, col, and index of the char in the word we are searching for.
        # keep track of the visited cells so we don't run into an infinite loop
        # need to restore the value of the cell to the previous leeter after the recursive calls have finished.

        rows, cols = len(board), len(board[0])

        def dfs(r, c, index):
            if index == len(word):
                return True
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != word[index]:
                return False

            temp = board[r][c]
            board[r][c] = '#'
            # finish dfs
            # return found

        # init dfs from each of the cells that have first letter of word
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0]:
                    if dfs(row, col, 0):
                        return True

        return false