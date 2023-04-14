class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def inBound(row, col):
            return (0 <= row < len(grid)) and (0 <= col < len(grid[0]))
        
        def findArea(visited, row, col, maxArea):
            if grid[row][col] == 0:
                return 0
            
            visited[row][col] = 1
            area = 1
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            
            for rowChange, colChange in directions:
                newRow = row + rowChange
                newCol = col + colChange
                
                if inBound(newRow, newCol) and visited[newRow][newCol] == 0:
                    area += findArea(visited, newRow, newCol, maxArea)
                    
            maxArea[0] = max(maxArea[0], area)
            return area
        
        visited = [[0 for col in range(len(grid[0]))] for row in range(len(grid))]
        maxArea = [0]
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                findArea(visited, row, col, maxArea)
                
        return maxArea[0]
        
            
                    
            
                
                
            
        