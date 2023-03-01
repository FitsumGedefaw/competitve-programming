class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        
        else:
            res = [1] * (rowIndex+1)
            
            prevRow = self.getRow(rowIndex-1)
            
            for i in range(1, len(res)-1):
                res[i] = prevRow[i-1] + prevRow[i]
                
            return res
        