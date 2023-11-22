class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        n, m = len(board), len(board[0])
        numOfBattleships = 0

        for row in range(n):
            for col in range(m):
    
                if board[row][col] == "X" and (row == 0 or board[row - 1][col] == ".") and (col == 0 or board[row][col - 1] == "."):
                  numOfBattleships += 1

        return numOfBattleships  

