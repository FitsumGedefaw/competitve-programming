class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        mtPeakIdx = mtEndIdx = -1
        
        for i in range(len(arr)-1):
            if arr[i] == arr[i+1]:
                return False
            elif arr[i] > arr[i+1]:
                mtPeakIdx = i
                break
        
        if mtPeakIdx in [-1, 0]:
            return False
        
        for i in range(mtPeakIdx+1, len(arr)-1):
            if arr[i] <= arr[i+1]:
                return False
        
        return True
            
            