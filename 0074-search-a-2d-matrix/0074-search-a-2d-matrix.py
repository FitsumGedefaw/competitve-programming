class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        candidateRowInd = -1
        
        for rowInd in range(len(matrix)):
            if matrix[rowInd][-1] >= target:
                candidateRowInd = rowInd
                break
                
        if candidateRowInd == -1:
            return False
        else:
            numsInRow = set(matrix[candidateRowInd])
            
            if target in numsInRow:
                return True
            else:
                return False
                