class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = []
        
        low, high = 0, len(nums)-1
        while low <= high:
            mid = low+(high-low)//2
            if nums[mid] < target:
                low = mid+1
            elif nums[mid] > target:
                high = mid-1
            else:
                left, right = low, mid
                while left < right:
                    m = left+(right-left)//2
                    if nums[m] == target:
                        right = m
                    else:
                        left = m+1
                ans.append(left)
                
                left, right = mid, high
                while left <= right:
                    m = left+(right-left)//2
                    if nums[m] == target:
                        left = m+1
                    else:
                        right = m-1
                ans.append(left-1)
                return ans
                
        return [-1, -1]
                
            
        