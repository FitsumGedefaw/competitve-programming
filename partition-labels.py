class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        size = end = 0
        res = []
        lastIndex = defaultdict(int)
        for index, char in enumerate(s):
            lastIndex[char] = index
        for i in range(len(s)):
            size += 1
            end = max(end, lastIndex[s[i]])
            if end == i:
                res.append(size)
                size = 0
        return res
                
            
        
