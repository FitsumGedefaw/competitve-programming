t = int(input())

for _ in range(t):
    n, m = [int(num) for num in input().split()]

    matrix = []

    for i in range(n):
        matrix.append([int(num) for num in input().split()])

    left_diagonal_sum = {}
    right_diagonal_sum = {}

    #Let's store the sum of each left diagonal and each right diagonal in the matrix
    for rowIdx in range(n):
        for colIdx in range(m):
            left_diagonal_sum[rowIdx+colIdx] = left_diagonal_sum.get(rowIdx+colIdx, 0) + matrix[rowIdx][colIdx] 

            right_diagonal_sum[rowIdx-colIdx] = right_diagonal_sum.get(rowIdx-colIdx, 0) + matrix[rowIdx][colIdx] 

    #So, which cell has the maximum diagonal sum, considering both its left and right diagonals? Extract the maximum sum!
    maxSum = 0

    for rowIdx in range(n):
        for colIdx in range(m):
            maxSum = max(maxSum, left_diagonal_sum[rowIdx+colIdx] + right_diagonal_sum[rowIdx-colIdx] - matrix[rowIdx][colIdx])

    print(maxSum)

    




    

