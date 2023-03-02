class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def predictor(left, right, turn, score1, score2):
            #score1: score of player1     score2: score of player2
            
            if left > right:
                #Every number is taken, so no number to choose
                return score1 >= score2
            
            if turn:  #player1's turn
                #player1 chooses a number(from the ends), updates the pointers, and gives the #turn to player2
                return predictor(left+1, right, 0, score1+nums[left], score2) or predictor(left, right-1, 0, score1+nums[right], score2)
            
            #player2's turn
            #player2 chooses a number(from the ends), updates the pointers, and gives the turn #to player2
            return predictor(left+1, right, 1, score1, score2+nums[left]) and predictor(left, right-1, 1, score1, score2+nums[right])
        
        #The game starts!
        return predictor(0, len(nums)-1, 1, 0, 0)            
            
            
        