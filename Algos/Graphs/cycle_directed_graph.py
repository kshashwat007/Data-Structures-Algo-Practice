# https://www.geeksforgeeks.org/detect-cycle-in-a-graph/
def cycleInGraph(edges):
    visited = [False] * (len(edges))
    stack = [False] * (len(edges))
    for node in range(len(edges)):
        if visited[node]:
            continue
        cycleGraph = cycleUtil(visited, stack, edges, node)
        if cycleGraph:
            return True
    return False


def cycleUtil(visited, stack, edges, node):
    visited[node] = True
    stack[node] = True
    for neighbor in edges[node]:
        if visited[neighbor] == False:
            cycleGraph = cycleUtil(visited, stack, edges, neighbor)
            if cycleGraph:
                return True
        elif stack[neighbor] == True:
            return True
    stack[node] = False
    return False


edges1 = [
    [],
    [0, 3],
    [0],
    [1, 2]
]
print(cycleInGraph(edges1))
