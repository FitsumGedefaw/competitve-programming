class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        
        #Time Complexity: O((n**2)(m))
        #Space Complexity: O(1)
        answer = 0
        
        while len(grid[0]) > 0: 
            maxDeletedNum = float('-inf')
            
            for row in grid:
                maxInRow = max(row)
                
                maxDeletedNum = max(maxDeletedNum, maxInRow)
                
                row.remove(maxInRow)
            
            answer += maxDeletedNum
        
        return answer