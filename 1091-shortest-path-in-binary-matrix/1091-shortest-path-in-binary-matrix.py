class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        
        minLen = -1
        visited = [[0 for col in range(n)] for row in range(n)]
        visited[0][0] = 1
        
        def inBound(row, col):
            return (0 <= row < n) and (0 <= col < n)
        
        def isValid(row, col):
            if not inBound(row, col) or visited[row][col] == 1 or grid[row][col] == 1:
                return False
            return True
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        
        queue = deque([(0, 0, 1)])
        
        while queue:
            row, col, level = queue.popleft()
            
            if row == n-1 and col == n-1:
                return level
            
            for colChange, rowChange in directions:
                newRow = row + rowChange
                newCol = col + colChange   
                
                if isValid(newRow, newCol):
                    queue.append((newRow, newCol, level+1))
                    visited[newRow][newCol] = 1
                
        return -1
               
            
        
        