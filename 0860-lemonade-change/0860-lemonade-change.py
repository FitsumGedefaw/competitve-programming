class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count = {5: 0, 10: 0}
        
        for bill in bills:
            if bill == 5:
                count[5] += 1
            
            elif bill == 10:
                if count[5] > 0:
                    count[5] -= 1
                    count[10] += 1
                else:
                    return False
            
            elif bill == 20:
                if count[10] > 0 and count[5] > 0:
                    count[10] -= 1
                    count[5] -= 1
                
                elif count[5] >= 3:
                    count[5] -= 3
                    
                else:
                    return False
                
        return True
                    
        
        