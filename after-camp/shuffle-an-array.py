class Solution:

    def __init__(self, nums: List[int]):
        self.original = nums
        self.arr = list(nums)        

    def reset(self) -> List[int]:
        self.arr = list(self.original)
        return self.arr

    def shuffle(self) -> List[int]:
        for i in range(len(self.arr)):
            chosenIdx = random.randrange(i, len(self.arr))
            self.arr[i], self.arr[chosenIdx] = self.arr[chosenIdx], self.arr[i]
        
        return self.arr

    
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()