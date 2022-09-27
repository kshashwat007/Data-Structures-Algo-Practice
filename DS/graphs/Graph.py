from collections import defaultdict
import collections


class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def find_parent(self, parent, i):
        if parent[i] == -1:
            return i
        if parent[i] != -1:
            return self.find_parent(parent, parent[i])

    def union(self, parent, x, y):
        parent[x] = y

    def isCyclic(self):
        parent = [-1] * (self.V)
        for i in self.graph:
            for j in self.graph[i]:
                x = self.find_parent(parent, i)
                y = self.find_parent(parent, j)
                if x == y:
                    return True
                self.union(parent, x, y)

    def dfs(self):
        visited = []
        for vertex in self.graph:
            if vertex not in visited:
                self.dfsutil(vertex, visited)
        return visited

    def dfsutil(self, node, visited):
        visited.append(node)
        for neighbour in self.graph[node]:
            if neighbour not in visited:
                self.dfsutil(neighbour, visited)

    def dfs_iter(self, root):
        visited = []
        stack = [root]
        while stack:
            v = stack.pop()
            if v not in visited:
                visited.append(v)
                for neighbour in self.graph[v]:
                    if neighbour not in visited:
                        stack.append(neighbour)

    def bfs(self, node):
        visited = []
        queue = []
        visited.append(node)
        queue.append(node)
        while queue:
            s = queue.pop(0)
            if s not in visited:
                visited.append(s)
            for neighbour in self.graph[s]:
                if neighbour not in visited:
                    queue.append(neighbour)
        return visited


g = Graph(6)
g.addEdge(0, 1)
g.addEdge(2, 1)
g.addEdge(3, 1)
g.addEdge(4, 1)
g.addEdge(5, 4)
# print("DFS of graph is", g.dfs())
print("BFS of graph is", g.bfs(0))
if g.isCyclic():
    print("Graph contains cycle")
else:
    print("No cycle")
