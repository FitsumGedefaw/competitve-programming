import heapq
class Solution(object):
    def kClosest(self, points, k):
        temp = []
        for x, y in points:
            d = (x**2) + (y**2)
            temp.append([d, x, y])
        heapq.heapify(temp)
        result = []
        for i in range(k):
            d, x, y = heapq.heappop(temp)
            result.append([x, y])
        return result
