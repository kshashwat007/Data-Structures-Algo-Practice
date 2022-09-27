from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def topological_sort(self):
        ordering = []
        stack = []
        visited = [False] * self.V
        for i in range(self.V):
            if visited[i] == False:
                self.topological_sort_util(i, stack, visited)
        while stack:
            ordering.append(stack.pop())
        return ordering

    def topological_sort_util(self, v, stack, visited):
        visited[v] = True
        for i in self.graph[v]:
            if visited[i] == False:
                self.topological_sort_util(i, stack, visited)
        stack.append(v)


g = Graph(6)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)

print(g.topological_sort())
