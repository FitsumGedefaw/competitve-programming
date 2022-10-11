class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        l = ans = 0
        while l < len(arr)-1:
            if arr[l] < arr[l+1]:
                temp = 1
                while l < len(arr)-1 and arr[l] < arr[l+1]:
                    l, temp = l+1, temp+1
                if l < len(arr)-1 and arr[l] > arr[l+1]:
                    while l < len(arr)-1 and arr[l] > arr[l+1]:
                        l, temp = l+1, temp+1
                    ans = max(ans, temp)
            else:
                l += 1
        return ans
                
        
        
        
        
