class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        prev = 0
        for num in arr:
            if num - prev > 1:
                if num - prev - 1 >= k:
                    return prev + k
                k -= num - prev - 1
            prev = num

        return prev + k

        