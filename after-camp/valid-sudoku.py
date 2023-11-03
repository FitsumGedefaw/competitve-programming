class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            nums = [x for x in row if x != "."]
            if len(nums) != len(set(nums)):
                return False
            
        for col in zip(*board):
            nums = [x for x in col if x != "."]
            if len(nums) != len(set(nums)):
                return False
            
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                nums = [board[r][c] for r in range(i, i+3) for c in range(j, j+3) if board[r][c] != "."]
                if len(nums) != len(set(nums)):
                    return False
        
        return True