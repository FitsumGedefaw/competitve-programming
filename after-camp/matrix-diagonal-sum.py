class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        row = 0
        col = 0
        res = 0
        if n == 1:
            return mat[0][0]

        while row < n and col < n:
            res += mat[row][col]
            row, col = row + 1, col + 1
        
        row = 0
        col = n - 1
        while row < n and col >= 0:
            res += mat[row][col]
            row , col = row + 1, col - 1

        if n % 2 == 0:
            return res
        else:
            mid = (n -1) // 2
            return res - mat[mid][mid]
        

        