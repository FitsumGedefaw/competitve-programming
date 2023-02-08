class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        numOfMSqs = 0
        
        for startRow in range(0, m-2):
            for startCol in range(0, n-2):
                
                #Check if all elements in the subgrid are distinct and in range [1, 9]
                subgridElements = {grid[r][c] for r in range(startRow, startRow+3) for c in range(startCol, startCol+3) if grid[r][c] >= 1 and grid[r][c] <= 9} 
                    
                if len(subgridElements) < 9:
                    continue
                
                else:
                    F = 1
                    _sum = grid[startRow][startCol] + grid[startRow][startCol+1] + grid[startRow][startCol+2]
                    
                    #Check if each of the rows in the subgrid have  the same sum
                    for r in range(startRow+1, startRow+3):
                        rowSum = sum(grid[r][c] for c in range(startCol, startCol+3))
                        if rowSum != _sum:
                            F = 0
                            break
                            
                    #Check if each of the columns in the subgrid have  the same sum
                    if F == 1:
                        for c in range(startCol, startCol+3):
                            colSum = sum(grid[r][c] for r in range(startRow, startRow+3))
                            if colSum != _sum:
                                F = 0
                                break
                    
                    #Check if each of the diagonals in the subgrid have  the same sum
                    if F == 1:
                        d1Sum = grid[startRow][startCol] + grid[startRow+1][startCol+1] + grid[startRow+2][startCol+2]
                        if d1Sum != _sum:
                            F = 0
                      
                    if F == 1:
                        d2Sum = grid[startRow][startCol+2] + grid[startRow+1][startCol+1] + grid[startRow+2][startCol]
                        if d2Sum != _sum:
                            F = 0
                            
                    if F == 1:
                        numOfMSqs += 1
                        
        return numOfMSqs
                        
                            
                            
                        
                    
                    
            