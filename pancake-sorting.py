class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def flip(r):
            l = 0
            while l < r:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1
        result = []
        N = len(arr)
        for i in range(N, 0, -1):
            subArr = arr[:i]
            maxIndex = arr.index(max(subArr))
            if maxIndex != i - 1:
                flip(maxIndex)
                flip(i-1)
                result.append(maxIndex+1)
                result.append(i)
        return result
