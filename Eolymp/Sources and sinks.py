def connectionExists(arr):
    for num in arr:
        if num == 1:
            return True
    return False

n = int(input())
adjMat = []
for _ in range(n):
    row = [int(num) for num in input().split()]
    adjMat.append(row)

adjMatT = list(zip(*adjMat))
sources = []
sinks = []

for i in range(len(adjMat)):
    if connectionExists(adjMat[i]):
        if not connectionExists(adjMatT[i]):
            sources.append(i + 1)
    
    else:
        if not connectionExists(adjMatT[i]):
            sources.append(i + 1)
        sinks.append(i + 1)

print(len(sources), *sources)
print(len(sinks), *sinks)
