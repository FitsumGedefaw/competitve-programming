class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        position = 1
        h = 0
        for num in citations:
            if num >= position:
                h += 1
                position += 1
            else:
                break
        return h
