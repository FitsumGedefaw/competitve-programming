n, m = [int(num) for num in input().split()]

grid = []

for _ in range(n):
    grid.append(list(input()))

crossedCells = set()

for row in range(n):
    lettersInRow = {}

    for col in range(m):
        if grid[row][col] not in lettersInRow:
            lettersInRow[grid[row][col]] = row*m + col

        else:
            crossedCells.add(lettersInRow[grid[row][col]])
            crossedCells.add(row*m + col)

for col in range(m):
    lettersInCol = {}

    for row in range(n):
        if grid[row][col] not in lettersInCol:
            lettersInCol[grid[row][col]] = row*m + col

        else:
            crossedCells.add(lettersInCol[grid[row][col]])
            crossedCells.add(row*m + col)

ans = ""
for rowIdx in range(n):
    for colIdx in range(m):
        if (rowIdx*m + colIdx) not in crossedCells:
            ans += grid[rowIdx][colIdx]
            
print(ans) 





