class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr) == 1:
            return [-1]
        
        else:
            rightMax = arr[-1]
            
            arr[-1] = -1
            
            for i in range(len(arr)-2, -1, -1):
                num = arr[i]
                
                arr[i] = rightMax
                
                rightMax = max(rightMax, num)
                
        return arr
                
                
        