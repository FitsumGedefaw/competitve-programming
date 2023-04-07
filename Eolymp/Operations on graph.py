from collections import defaultdict


n = int(input())
k = int(input())

graph = defaultdict(list)

for _ in range(k):
    op = [int(num) for num in input().split()]
    if op[0] == 1:
        graph[op[1]].append(op[2])
        graph[op[2]].append(op[1])
    
    else:
        print(*graph[op[1]])
