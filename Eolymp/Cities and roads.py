from collections import defaultdict


n = int(input())
graph = defaultdict(list)

for i in range(n):
    row = [num for num in input().split()]

    for j in range(i+1, n):
        if row[j] == "1":
            graph[i].append(j)

numOfRoads = 0
for city in graph:
    numOfRoads += len(graph[city])

print(numOfRoads)
