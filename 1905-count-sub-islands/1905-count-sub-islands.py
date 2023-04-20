class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m, n = len(grid1), len(grid1[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        numOfSubIslands = 0
        
        def inBound(row, col):
            return (0 <= row < m) and (0 <= col < n)
        
        def dfs(row, col):
            grid2[row][col] = 0
            
            for rowChange, colChange in directions:
                newRow = row + rowChange
                newCol = col + colChange
                
                if inBound(newRow, newCol) and grid2[newRow][newCol] == 1:
                    dfs(newRow, newCol)
                    
        for row in range(m):
            for col in range(n):
                if grid2[row][col] == 1 and grid1[row][col] == 0:
                    dfs(row, col)
        
        for row in range(m):
            for col in range(n):
                if grid2[row][col] == 1:
                    numOfSubIslands += 1
                    dfs(row, col)
                    
        return numOfSubIslands
        
        
            
            
        
        
        
        