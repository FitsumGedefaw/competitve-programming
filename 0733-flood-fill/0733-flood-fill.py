class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visited = [ [0 for col in range(len(image[0]))] for row in range(len(image))]
        
        def inbound(row, col):
            return (0 <= row < len(image) and 0 <= col < len(image[0]))
        
        def gridDfs(grid, visited, row, col, color):
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            visited[row][col] = True
            
            for row_change, col_change in directions:
                new_row = row + row_change
                new_col = col + col_change
                
                if inbound(new_row, new_col) and not visited[new_row][new_col] and grid[new_row][new_col] == grid[row][col]:
                    gridDfs(grid, visited, new_row, new_col, color)
                    
            grid[row][col] = color
        
        
        
        gridDfs(image, visited, sr, sc, color)
        return image