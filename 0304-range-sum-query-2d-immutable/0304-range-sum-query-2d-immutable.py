class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matPrefixSum = matrix
        
        for row in range(len(self.matPrefixSum)):
            for col in range(len(self.matPrefixSum[0])):
                top = self.matPrefixSum[row-1][col] if row > 0 else 0
                left = self.matPrefixSum[row][col-1] if col > 0 else 0
                topleft = self.matPrefixSum[row-1][col-1] if row > 0 and col > 0 else 0
                
                self.matPrefixSum[row][col] = top + left - topleft + self.matPrefixSum[row][col]
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        topRegionSum = self.matPrefixSum[row1-1][col2] if row1 > 0 else 0
        leftRegionSum = self.matPrefixSum[row2][col1-1] if col1 > 0 else 0
        topleftRegionSum = self.matPrefixSum[row1-1][col1-1] if row1 > 0 and col1 > 0 else 0
        
        return self.matPrefixSum[row2][col2] - topRegionSum - leftRegionSum + topleftRegionSum
        
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)