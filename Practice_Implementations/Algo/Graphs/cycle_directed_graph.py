from curses import flash


def cycleInGraph(edges):
    stack = [False] * len(edges)
    visited = [False] * len(edges)

    for node in range(len(edges)):
        if visited[node]:
            continue
        cycle = cycleUtil(visited, stack, edges, node)
        if cycle:
            return True
    return False


def cycleUtil(visited, stack, edges, node):
    visited[node] = True
    stack[node] = True
    for neighbour in edges[node]:
        if visited[neighbour] == False:
            cycle = cycleUtil(visited, stack, edges, neighbour)
            if cycle:
                return True
        elif stack[neighbour] == True:
            return True
    stack[neighbour] = False
    return False


edges1 = [
    [],
    [0, 3],
    [0],
    [1, 2]
]
print(cycleInGraph(edges1))
