from collections import defaultdict


class Solution:
    def canFinish(self, numCourses, prerequisites):
        graph = defaultdict(list)
        visited = [False] * numCourses
        stack = [False] * numCourses
        res = []

        def checkCycle(node):
            visited[node] = True
            stack[node] = True
            for neighbor in graph[node]:
                if visited[neighbor] == False:
                    cycleCheck = checkCycle(neighbor)
                    if cycleCheck:
                        return True
                elif stack[neighbor] == True:
                    return True
            stack[node] = False
            res.append(node)
            return False

        for x, y in prerequisites:
            graph[y].append(x)

        for node in range(numCourses):
            if visited[node] == True:
                continue
            cycleCheck = checkCycle(node)
            if cycleCheck:
                return False

        print(res[::-1])
        return True


s = Solution()
n = 4
prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
print(s.canFinish(n, prerequisites))
