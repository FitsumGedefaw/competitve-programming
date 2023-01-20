class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for rowIdx in range(1, len(matrix)):
            for colIdx in range(1, len(matrix[0])):
                
                if matrix[rowIdx][colIdx] != matrix[rowIdx-1][colIdx-1]:
                    return False
            
        return True