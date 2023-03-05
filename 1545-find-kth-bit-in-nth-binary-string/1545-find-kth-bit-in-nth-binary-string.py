class Solution:
    def revInvBinStr(self, s):
        arr = deque()
        for ch in s:
            if ch == "0":
                arr.appendleft("1")
            else:
                arr.appendleft("0")
        
        return "".join(arr)
    
    def findNthBinStr(self, n):
        if n == 1:
            return "0"
        
        binStr = self.findNthBinStr(n-1)
        
        return binStr + "1" + self.revInvBinStr(binStr)
            
    def findKthBit(self, n: int, k: int) -> str:
        nthBinStr = self.findNthBinStr(n)
        
        return nthBinStr[k-1]
        
        