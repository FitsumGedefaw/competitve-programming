class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        res = []
        if len(changed) % 2 != 0:
            return []
        changed.sort()
        d = defaultdict(int)
        for v in changed:
            d[v] = d[v] + 1
        for i in range(len(changed)):
            if d[changed[i]] > 0:
                if d[2*changed[i]] > 0:
                    res.append(changed[i])
                    d[changed[i]] -= 1
                    d[2*changed[i]] -= 1
                else: 
                    return []
        return res
        
        
        