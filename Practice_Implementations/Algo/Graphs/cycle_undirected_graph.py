from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def isCyclic(self):
        visited = {}
        for i in range(self.V):
            if i not in visited:
                return self.isCyclicUtil(i, visited, -1)

    def isCyclicUtil(self, node, visited, parent):
        visited[node] = True
        for neighbour in self.graph[node]:
            if neighbour not in visited:
                self.isCyclicUtil(neighbour, visited, node)
            elif neighbour != parent:
                return True
        return False


g = Graph(5)
g.addEdge(1, 0)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(0, 3)
g.addEdge(3, 4)
g1 = Graph(3)
g1.addEdge(0, 1)
g1.addEdge(1, 2)
print(g.isCyclic())
print(g1.isCyclic())
