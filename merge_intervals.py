class Solution(object):
    def merge(self, intervals):
        intervals.sort();
        result = [intervals[0]]
        for start, end in intervals[1 : ]:
            lastEnd = result[-1][1]
            if start <= lastEnd:
                result[-1][1] = max(end, lastEnd)
            else:
                result.append([start, end])
        return result
