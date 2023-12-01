class Solution:
    def arrangeCoins(self, n: int) -> int:
        low, high = 1, n / 2

        while low < high:
            mid = math.ceil(low + (high - low) / 2)
            if (mid / 2) * (1 + mid) <= n:
                low = mid
            else:
                high = mid - 1
        
        return low

