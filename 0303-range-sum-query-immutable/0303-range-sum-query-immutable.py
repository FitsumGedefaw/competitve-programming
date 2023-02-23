class NumArray:

    def __init__(self, nums: List[int]):
        self.arr = nums
        
        _sum = 0
        for i in range(len(self.arr)):
            _sum += self.arr[i]
            self.arr[i] = _sum
        

    def sumRange(self, left: int, right: int) -> int:
        res = self.arr[right] - self.arr[left-1] if left > 0 else self.arr[right]
        return res

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)