class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        while k > 0:
            v = nums.pop()
            nums.insert(0,v)
            k -= 1
        
        