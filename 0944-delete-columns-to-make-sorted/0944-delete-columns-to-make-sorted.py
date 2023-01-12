class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        numOfCols = 0
        
        for i in range(len(strs[0])):
            for j in range(len(strs)-1):
                if strs[j][i] <= strs[j+1][i]:
                    continue
                else:
                    numOfCols += 1
                    break
                    
        return numOfCols
                    