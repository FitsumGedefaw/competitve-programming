class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        l , r , score = 0 , len(tokens) - 1 , 0
        if len(tokens) == 0 or power < tokens[0]:
                return 0   
        while l <= r:
            if power >= tokens[l]:
                power -= tokens[l]
                l , score = l + 1, score + 1
            elif power < tokens[l] and l != r:
                power += tokens[r] - tokens[l]
                l, r = l + 1, r - 1
            else:
                break
        return score
                
        
