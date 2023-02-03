class Solution:
    def flip(self, l, r, arr):
        while l <  r:
            arr[l], arr[r] = arr[r], arr[l]
            l, r = l+1, r-1
            
    def pancakeSort(self, arr: List[int]) -> List[int]:
        flipSequence = []
        
        p = len(arr)-1
        val = len(arr)
        
        while p >= 0:
            
            idx = arr.index(val)
            
            self.flip(0, idx, arr)
            flipSequence.append(idx+1)
            
            self.flip(0, p, arr)
            flipSequence.append(p+1)
            
            p, val = p-1, val-1
         
        return flipSequence
            