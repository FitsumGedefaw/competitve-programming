class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #Time Complexity = O(m * n)
        #Space Complexity = O(m + n)
        
        m = len(matrix)
        n = len(matrix[0])
        
        rowsTobeZero = set()
        colsTobeZero = set()
        
        for rowIdx in range(m):
            for colIdx in range(n):
                if matrix[rowIdx][colIdx] == 0:
                    rowsTobeZero.add(rowIdx)
                    colsTobeZero.add(colIdx)
                    
        for rowIdx in rowsTobeZero:
            for colIdx in range(n):
                matrix[rowIdx][colIdx] = 0
                
        for colIdx in colsTobeZero:
            for rowIdx in range(m):
                matrix[rowIdx][colIdx] = 0
                
                    