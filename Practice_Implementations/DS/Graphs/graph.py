from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, root):
        stack = [root]
        visited = []
        while stack:
            v = stack.pop()
            if v not in visited:
                visited.append(v)
                for neighbour in self.graph[v]:
                    if neighbour not in visited:
                        stack.append(neighbour)

    def dfs(self):
        visited = []
        for vertex in self.graph:
            if vertex not in visited:
                self.dfs_util(visited, vertex)
        return visited

    def dfs_util(self, visited, v):
        visited.append(v)
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.dfs_util(visited, neighbour)

    def bfs(self, root):
        visited, queue = [root], [root]
        while queue:
            v = queue.pop(0)
            if v not in visited:
                visited.append(v)
            for neighbour in self.graph[v]:
                if neighbour not in visited:
                    queue.append(neighbour)
        return visited
