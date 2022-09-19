class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        val = len(arr)
        for i in range(len(arr) - 1, -1, -1):
            valInd = arr.index(val)
            if valInd != i:
                l, r = 0, valInd
                while l < r:
                    arr[l], arr[r] = arr[r], arr[l]
                    l, r = l + 1, r - 1
                res.append(valInd + 1)
                left, right = 0, i
                while left < right:
                    arr[left], arr[right] = arr[right], arr[left]
                    left, right = left + 1, right - 1
                res.append(i + 1)
            val -= 1
        return res
