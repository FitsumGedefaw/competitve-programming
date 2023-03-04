class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        res = [0] * 1001
        for n, s, e in trips:
            res[s] += n
            res[e] -= n
        if res[0] > capacity:
            return False
        for i in range(1, len(res)):
            res[i] += res[i-1]
            if res[i] > capacity:
                return False
        return True
            