class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = str(x)
        left, right = 0, len(num)-1
        
        while left < right:
            if num[left] != num[right]:
                return False
            
            left, right = left+1, right-1
            
        return True
        
        
        