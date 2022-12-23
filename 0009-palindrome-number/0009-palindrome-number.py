class Solution:
    def isPalindrome(self, x: int) -> bool:
        reversedNum = 0
        
        if x < 0:
            return False
    
        originalNum = x
        
        while x != 0:
            lastDigit = x % 10
            
            reversedNum = (reversedNum * 10) + lastDigit
            
            x = x // 10
        
        return originalNum == reversedNum 
        
        