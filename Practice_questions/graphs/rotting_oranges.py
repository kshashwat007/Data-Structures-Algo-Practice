# You are given an m x n grid where each cell can have one of three values:

# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

#   gridEx = [
#     [2, 1, 1]
#     [1, 1, 0]
#     [0, 1, 1]
# ]
# https://leetcode.com/problems/rotting-oranges/
class Solution:
    def orangesRotting(self, grid):
        rows, cols = len(grid), len(grid[0])
        mins = 0
        fresh = 0
        queue = []

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    queue.append((r, c))

        print("queue", queue)
        print("fresh total", fresh)

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while fresh > 0 and queue:
            for i in range(len(queue)):
                r, c = queue.pop(0)
                for dr, dc in directions:
                    row, col = r+dr, c+dc

                    if (
                        row in range(rows)
                        and col in range(cols)
                        and grid[row][col] == 1
                    ):
                        print("grid", grid[row][col], row, col)
                        print(fresh)
                        grid[row][col] = 2
                        queue.append((row, col))
                        fresh -= 1
                print(queue, fresh)
            mins += 1

        return mins if fresh == 0 else -1


grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
s = Solution()
print(s.orangesRotting(grid))
