class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        
        if (m * n) != (r * c):
            return mat
        
        else:
            numsInMat = [mat[rowIdx][colIdx] for rowIdx in range(m) for colIdx in range(n)]
        
            reshapedMat = []
        
            i = 0
            while i < len(numsInMat):
                row = []
            
                for colIdx in range(i, i+c):
                    row.append(numsInMat[colIdx])
            
                reshapedMat.append(row)
            
                i += c
        
            return reshapedMat
        
        