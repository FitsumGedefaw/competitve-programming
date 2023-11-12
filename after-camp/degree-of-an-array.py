class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        ans = 1
        d = {}
        maxFreq = 1
        for idx, val in enumerate(nums):
            if val not in d:
                d[val] = (1, idx, idx)

            else:
                d[val] = (d[val][0] + 1, d[val][1], idx)
                currFreq = d[val][0]
                if currFreq == maxFreq:
                    ans = min(ans, d[val][2] - d[val][1] + 1)
                elif currFreq > maxFreq:
                    ans = d[val][2] - d[val][1] + 1
                    maxFreq = currFreq
        return ans



            

        