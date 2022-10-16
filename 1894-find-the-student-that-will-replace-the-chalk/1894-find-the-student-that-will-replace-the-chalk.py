class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        totalSum = 0
        for num in chalk:
            totalSum += num
        r = k % totalSum
        for i in range(len(chalk)):
            if chalk[i] > r:
                return i
            r -= chalk[i]

        
        