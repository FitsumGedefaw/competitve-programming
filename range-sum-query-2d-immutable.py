class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.psa = []
        for i in range(len(matrix)):
            preSum = [matrix[i][0]]
            for j in range(1, len(matrix[i])):
                preSum.append(preSum[-1] + matrix[i][j])
            self.psa.append(preSum)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        self.ans = 0
        if col1 == 0:
            for i in range(row1, row2 + 1):
                self.ans += self.psa[i][col2]
        else:
            for i in range(row1, row2 + 1):
                self.ans += self.psa[i][col2] - self.psa[i][col1 - 1]
        return self.ans


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
