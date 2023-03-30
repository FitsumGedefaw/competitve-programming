class Solution:
    def bitwiseComplement(self, n: int) -> int:
        n = bin(n)
        comp = []
        
        for i in range(2, len(n)):
            if n[i] == "0":
                comp.append("1")
            else:
                comp.append("0")
                        
        return int("".join(comp), 2)