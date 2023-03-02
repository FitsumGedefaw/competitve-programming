class Solution:
    def revHelper(self, left, right, s):
        if left >= right:
            return 
        
        s[left], s[right] = s[right], s[left]
        self.revHelper(left+1, right-1, s)
            
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        self.revHelper(0, len(s)-1, s)
        
        