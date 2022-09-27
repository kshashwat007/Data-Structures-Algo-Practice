# https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid):
        if not grid or not grid[0]:
            return 0
        area = 0
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def isValid(r, c):
            return r in range(rows) and c in range(cols) and grid[r][c] == 1 and (r, c) not in visited

        def dfs(r, c):
            if not isValid(r, c):
                return 0
            visited.add((r, c))
            return 1 + dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    tot_area = dfs(r, c)
                    area = max(area, tot_area)
        return area


s = Solution()
grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
print(s.maxAreaOfIsland(grid))
