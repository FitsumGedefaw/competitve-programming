class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        intCount  = Counter(arr)
        intCountSorted = sorted(intCount, key=lambda x: intCount[x], reverse=True)
        result = 0
        count = len(arr)
        halfAmount = count/2
        for k in intCountSorted:
            if count <= halfAmount:
                break
            count -= intCount[k]
            result += 1
        return result
