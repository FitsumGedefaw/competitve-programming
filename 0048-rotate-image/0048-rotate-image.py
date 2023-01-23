class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """        
        n = len(matrix)
        
        matrixT = list(zip(*matrix))
                
        for rowIdx in range(n):
            colIdx = 0
            
            for j in range(n-1, -1, -1):
                matrix[rowIdx][colIdx] = matrixT[rowIdx][j]
                colIdx += 1
            
            
        

            
        
        
        