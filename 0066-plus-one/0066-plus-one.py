class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ""
    
        for digit in digits:
            num += str(digit)
        
        num = int(num) + 1
        num = str(num)
        
        digits = [int(d) for d in num]
        return digits
        