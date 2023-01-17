class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        
        #Time Complexity: O(n**4)
        #Space Complexity: O(n) 
        
        n = len(grid)
        
        maxLocal = []
        
        # i is the topleft row index
        for i in range(n-2):
            maxLocalRow = []
            
            #j is the topleft column index
            for j in range(n-2):
                matrixValues = set()
                
                matrixValues.add(grid[i][j])
                matrixValues.add(grid[i][j + 1])
                matrixValues.add(grid[i][j + 2])
                
                matrixValues.add(grid[i + 1][j])
                matrixValues.add(grid[i + 1][j + 1])
                matrixValues.add(grid[i + 1][j + 2])
                
                matrixValues.add(grid[i + 2][j])
                matrixValues.add(grid[i + 2][j + 1])
                matrixValues.add(grid[i + 2][j + 2])
                
                maxLocalRow.append(max(matrixValues))

            maxLocal.append(maxLocalRow)
            
        return maxLocal
                
                
                
            
                
                
            