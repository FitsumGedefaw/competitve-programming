from collections import defaultdict


while True:
    numOfNodes = int(input())
    if numOfNodes == 0:
        break

    numOfEdges = int(input())
    graph = defaultdict(list)
    color = {}

    for _ in range(numOfEdges):
        node1, node2 = [int(val) for val in input().split()]
        graph[node1].append(node2)
        graph[node2].append(node1)

    def colorNodes(node, nodeColor):
        color[node] = nodeColor

        for neighbour in graph[node]:
            if neighbour in color and color[neighbour] == nodeColor:
                return False
            if neighbour not in color:
                if colorNodes(neighbour, 1 - nodeColor) == False:
                    return False

        return True
    
    if colorNodes(1, 1):
        print("BICOLOURABLE.")
    else:
        print("NOT BICOLOURABLE.")
