class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        #n = trips[-1][2] - trips[0][1] + 1
        res = [0] * 1001
        for p,x,y in trips:
            res[x] += p
            #if y < n-1:
            res[y] -= p
        for i in range(1, len(res)):
            res[i] += res[i-1]
        ans = True
        for i in range(len(res)):
            if res[i] > capacity:
                return False
        return ans
