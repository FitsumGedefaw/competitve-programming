class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsCounted = Counter(nums)
        numsCountedSorted = sorted(numsCounted, key=lambda k: numsCounted[k], reverse=True)
        result = []
        for i in range(0,k):
            result.append(numsCountedSorted[i])
        return result
            
                    