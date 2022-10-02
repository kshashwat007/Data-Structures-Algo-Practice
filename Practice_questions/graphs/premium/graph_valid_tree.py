# https://www.lintcode.com/problem/178/
# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

# Input: n = 5 edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
# Output: true.

# Input: n = 5 edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
# Output: false.


# For a graph being a tree, we have to check the following things:-
# Checking how many connected components are present in the graph, It can only be a tree if it has only one connected component
# Checking if it has a cycle or not.

class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """

    def valid_tree(self, n, edges):

        parents = [i for i in range(n)]
        ranks = [1] * (n)

        def find(n):
            p = parents[n]
            while p != parents[p]:
                parents[p] = parents[parents[p]]
                p = parents[p]
            return p

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            print(n1, p1, n2, p2)
            if p1 == p2:
                return False
            if ranks[p1] > ranks[p2]:
                ranks[p1] += ranks[p2]
                parents[p2] = p1
            else:
                ranks[p2] += ranks[p1]
                parents[p1] = p2
            return True

        for x, y in edges:
            if not union(x, y):
                return False
        return True


s = Solution()
n = 5
edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
edges2 = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
edges3 = [[0, 1], [1, 2], [3, 2], [1, 3]]
print(s.valid_tree(n, edges3))
