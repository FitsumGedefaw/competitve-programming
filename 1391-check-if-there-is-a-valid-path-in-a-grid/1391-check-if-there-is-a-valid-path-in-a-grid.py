class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        rep = [[-1 for col in range(n)] for row in range(m)]
        
        def inBound(row, col):
            return 0 <= row < m and 0 <= col < n
        
        def markNodes(row, col):
            if inBound(row, col+1) and rep[row][col+1] == -1 and grid[row][col+1] in [1, 3, 5] and grid[row][col] in [1, 4, 6]:
                rep[row][col+1] = 0
                markNodes(row, col+1)
            
            if inBound(row, col-1) and rep[row][col-1] == -1 and grid[row][col-1] in [1, 4, 6] and grid[row][col] in [1, 3, 5]:
                rep[row][col-1] = 0
                markNodes(row, col-1)
                
            if inBound(row-1, col) and rep[row-1][col] == -1 and grid[row-1][col] in [2, 3, 4] and grid[row][col] in [2, 5, 6]:
                rep[row-1][col] = 0
                markNodes(row-1, col)
            
            if inBound(row+1, col) and rep[row+1][col] == -1 and grid[row+1][col] in [2, 5, 6] and grid[row][col] in [2, 3, 4]:
                rep[row+1][col] = 0
                markNodes(row+1, col)
                
        rep[0][0] = 0
        markNodes(0, 0)
        return rep[m-1][n-1] == 0
        
                