
# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to find the number of connected components in an undirected graph.
# Example 1:
#      0          3
#      |          |
#      1 --- 2    4
# Given n = 5 and edges = [[0, 1], [1, 2], [3, 4]], return 2.
# Example 2:
#      0           4
#      |           |
#      1 --- 2 --- 3
# Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]], return 1.
# Note:
# You can assume that no duplicate edges will appear inedges. Since all edges are undirected,[0, 1] is the same as [1, 0] and thus will not appear together in edges.

class Solution:
    def countComponents(self, n, edges):
        parents = [i for i in range(n)]
        ranks = [1] * (n)
        parent_count = set()

        def find(n):
            p = parents[n]
            while p != parents[p]:
                parents[p] = parents[parents[p]]
                p = parents[p]
            return p

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if ranks[p1] > ranks[p2]:
                ranks[p1] += ranks[p2]
                parents[p2] = p1
                parent_count.add(p1)
            else:
                ranks[p2] += ranks[p1]
                parents[p1] = p2
                parent_count.add(p2)

        for x, y in edges:
            union(x, y)
        print(parent_count)
        return len(parent_count)


s = Solution()
n = 5
edges = [[0, 1], [1, 2], [3, 4]]
print(s.countComponents(n, edges))
