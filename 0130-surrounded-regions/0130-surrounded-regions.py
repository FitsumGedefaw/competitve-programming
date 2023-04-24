class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def inBound(row, col):
            return (0 <= row < m) and (0 <= col < n)
           
        def markUnflippables(row, col):
            board[row][col] = "#"
            
            for rowChange, colChange in directions:
                newRow = row + rowChange
                newCol = col + colChange
                
                if not inBound(newRow, newCol) or board[newRow][newCol] != "O":
                    continue
                
                markUnflippables(newRow, newCol)
        
        for row in range(m):
            if board[row][0] == "O":
                markUnflippables(row, 0)
            if board[row][n-1] == "O":
                markUnflippables(row, n-1)
                
        for col in range(n):
            if board[0][col] == "O":
                markUnflippables(0, col)
            if board[m-1][col] == "O":
                markUnflippables(m-1, col)
        
        for row in range(m):
            for col in range(n):
                if board[row][col] == "O":
                    board[row][col] = "X"
                    
                elif board[row][col] == "#":
                    board[row][col] = "O"