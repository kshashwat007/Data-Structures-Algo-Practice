# https://www.lintcode.com/problem/663/
# You are given a m x n 2D grid initialized with these three possible values.

# -1 - A wall or an obstacle.
# 0 - A gate.
# INF - Infinity means an empty room. We use the value 2^31 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
# Fill each empty room with the distance to its nearest gate. If it is impossible to reach a Gate, that room should remain filled with INF

# Input:
# [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
# Output:
# [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]

# Explanation:
# the 2D grid is:

# INF  -1  0  INF
# INF INF INF  -1
# INF  -1 INF  -1
#   0  -1 INF INF

# the answer is:
#   3  -1   0   1
#   2   2   1  -1
#   1  -1   2  -1
#   0  -1   3   4

class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """

    def walls_and_gates(self, rooms):
        rows, cols = len(rooms), len(rooms[0])
        visited = set()
        queue = []
        dir = 1
        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    queue.append((r, c))
                    visited.add((r, c))

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while queue:

            for i in range(len(queue)):
                r, c = queue.pop(0)

                for dr, dc in directions:
                    row, col = r+dr, c+dc
                    if (
                        row in range(rows)
                        and col in range(cols)
                        and (row, col) not in visited
                        and rooms[row][col] != -1
                    ):
                        rooms[row][col] = dir
                        queue.append((row, col))
                        visited.add((row, col))
            dir += 1

        return rooms


class Solution1:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """

    def walls_and_gates(self, rooms):
        pass


rooms = [
    [2147483647, -1, 0, 2147483647],
    [2147483647, 2147483647, 2147483647, -1],
    [2147483647, -1, 2147483647, -1],
    [0, -1, 2147483647, 2147483647]]
s = Solution()
print(s.walls_and_gates(rooms))
