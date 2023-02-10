class Solution:
    def compare(self, a, b):
        if b+a >= a+b:
            return 1
        else:
            return -1
        
    def largestNumber(self, nums: List[int]) -> str:
        temp = sorted([str(num) for num in nums], key=cmp_to_key(self.compare))
        return str(int("".join(temp)))