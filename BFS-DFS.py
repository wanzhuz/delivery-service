def createAdjacencyList(map,loc):
    connections = []
    for connection in map:
        if connection[0] == loc:
            connections.append(connection[1])
        elif connection[1] == loc:
            connections.append(connection[0])
    return connections

def getEdges(map):
    edges = []
    for connection in map:
        if connection[0] not in edges:
            edges.append(connection[0])
        if connection[1] not in edges:
            edges.append(connection[1])
    return edges

"""
BFS
"""

def bfs(map, office):
    edges = getEdges(map)
    routes = dict()
    for edge in edges:
        path = []
        visited=[]
        queue = [(office, [office])]
        while queue:
            loc,path = queue.pop(0)
            if loc == edge:
                routes[edge] = path
                break
            visited.append(loc)
            adjacencyList = createAdjacencyList(map,loc)
            adjacencyList.sort()
            for item in adjacencyList:
                if item == edge:
                    path.append(item)
                    routes[edge] = path
                    break
                else:
                    if item not in visited:
                        queue.append((item, path + [item]))
    return routes

"""
DFS map
"""
def dfs(map, office):
    edges = getEdges(map)
    routes = dict()
    for edge in edges:
        path = []
        visited=[]
        stack = [(office, [office])]
        while stack:
            loc,path = stack.pop()
            if loc == edge:
                routes[edge] = path
                break
            visited.append(loc)
            adjacencyList = createAdjacencyList(map,loc)
            adjacencyList.sort()
            for item in adjacencyList:
                if item == edge:
                    path.append(item)
                    routes[edge] = path
                    break
                else:
                    if item not in visited:
                        stack.append((item, path + [item]))
    return routes
