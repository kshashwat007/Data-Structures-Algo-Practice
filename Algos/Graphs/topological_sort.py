from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def topological_sort(self):
        visited = [False] * self.V
        stack = []
        ordering = []
        for i in range(self.V):
            if visited[i] == False:
                self.topological_util(i, visited, stack)
        while stack:
            ordering.append(stack.pop())
        return ordering

    def topological_util(self, v, visited, stack):
        visited[v] = True
        for i in self.graph[v]:
            if visited[i] == False:
                self.topological_util(i, visited, stack)
        print(v)
        stack.append(v)
        print(stack)


g = Graph(6)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)

print(g.topological_sort())
