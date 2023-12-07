class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:

      pstore = {1: 0}

      def getpower(num):
        nonlocal pstore
        if num in pstore: return pstore[num]

        if num % 2 == 0: 
          power = 1 + getpower(num // 2)
        else:
          power = 1 + getpower(num * 3 + 1)
        
        pstore[num] = power
        return pstore[num]
      

      tmp = {num: getpower(num) for num in range(lo, hi+1)}
      tmp = sorted(tmp.items(), key=lambda x: x[1])
      
      return tmp[k-1][0]

      