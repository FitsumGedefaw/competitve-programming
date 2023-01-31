class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        res = 0
        delVals = {}
        
        for dVal in deliciousness:
            
            for k in range(22):
                if (2 ** k)-dVal in delVals:
                    res += delVals[ (2 ** k)-dVal ]
                
            delVals[dVal] = delVals.get(dVal, 0) + 1
            
        return res % (10**9 + 7)
                
                
        
        