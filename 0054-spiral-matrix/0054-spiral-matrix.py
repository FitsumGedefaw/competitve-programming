class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        
        rowStartIdx, rowEndIdx = 0, len(matrix)-1
        colStartIdx, colEndIdx = 0, len(matrix[0])-1
        
        while rowStartIdx <= rowEndIdx and colStartIdx <= colEndIdx:
            for c in range(colStartIdx, colEndIdx+1):
                res.append(matrix[rowStartIdx][c])
            
            for r in range(rowStartIdx+1, rowEndIdx+1):
                res.append(matrix[r][colEndIdx])
                
            if rowStartIdx != rowEndIdx:    
                for c in range(colEndIdx-1, colStartIdx-1, -1):
                    res.append(matrix[rowEndIdx][c])
            
            if colStartIdx != colEndIdx:
                for r in range(rowEndIdx-1, rowStartIdx, -1):
                    res.append(matrix[r][colStartIdx])
                
            rowStartIdx, rowEndIdx = rowStartIdx+1, rowEndIdx-1
            colStartIdx, colEndIdx = colStartIdx+1, colEndIdx-1
            
        return res

                
            