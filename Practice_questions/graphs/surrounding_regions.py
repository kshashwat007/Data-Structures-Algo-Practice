# https://leetcode.com/problems/surrounded-regions/

class Solution:
    def solve(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        visited = set()

        def isValid(r, c):
            return r in range(rows) and c in range(cols) and board[r][c] == "O" and (r, c) not in visited

        def dfs(r, c):
            if not isValid(r, c):
                return
            visited.add((r, c))
            board[r][c] = "T"
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in directions:
                dfs(r+dr, c+dc)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and r in [0, rows-1] or c in [0, cols-1] and (r, c) not in visited:
                    dfs(r, c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "T":
                    board[r][c] = "O"

        return board


grid = [["O", "O", "O"], ["O", "O", "O"], ["O", "O", "O"]]

s = Solution()
print(s.solve(grid))
# print(grid)
