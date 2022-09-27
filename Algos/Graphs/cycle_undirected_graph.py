from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    # https://www.geeksforgeeks.org/detect-cycle-undirected-graph/
    def isCyclic(self):
        # print(self.graph)
        recStack = [False] * (self.V)
        visited = {}
        for node in range(self.V):
            if node not in visited:
                return self.isCyclicUtil(node, visited, -1)

    def isCyclicUtil(self, node, visited, parent):
        visited[node] = True
        for neighbour in self.graph[node]:
            if neighbour not in visited:
                self.isCyclicUtil(neighbour, visited, node)
            # IMP:- If an adjacent vertex is visited and is not the parent of the current vertex from which it was visited, then it is a cycle. I.E the adjacent vertex was already visited from a different node which was the parent node.
            elif parent != neighbour:
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
