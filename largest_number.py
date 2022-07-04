class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i, val in enumerate(nums):
            nums[i] = str(val) 
        # Now nums is a string array
        def compare(str1, str2):
            if (str1 + str2) > (str2 + str1):
                return -1
            else:
                return 1
        sorted_nums = sorted(nums, key = cmp_to_key(compare))
        return str(int("".join(sorted_nums)))
