class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m, n = len(board), len(board[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]
        
        def inBound(row, col):
            return (0 <= row < m) and (0 <= col < n)
        
        def numOfAdjMines(row, col):
            res = 0
            for rowChange, colChange in directions:
                newRow = row + rowChange
                newCol = col + colChange
                
                if inBound(newRow, newCol) and board[newRow][newCol] == "M":
                    res += 1
            return res
        
        def dfs(row, col):
            if board[row][col] == "M":
                board[row][col] = "X"
                return
            
            if board[row][col] == "B" or board[row][col].isdigit():
                return
            
            adjMines = numOfAdjMines(row, col)
            
            if adjMines > 0:
                board[row][col] = str(adjMines)
                return
            
            board[row][col] = "B"
            
            for rowChange, colChange in directions:
                newRow = row + rowChange
                newCol = col + colChange
                
                if inBound(newRow, newCol):
                    dfs(newRow, newCol)
                    
        dfs(click[0], click[1])
        return board
            
                
                
                
        