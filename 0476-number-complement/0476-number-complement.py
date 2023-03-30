class Solution:
    def findComplement(self, num: int) -> int:
        num = bin(num)
        comp = []
        
        for i in range(2, len(num)):
            if num[i] == "0":
                comp.append("1")
            else:
                comp.append("0")
                        
        return int("".join(comp), 2)
                
        
        