class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2:
            return []
        changed.sort()
        count = Counter(changed)    
        result = []
        for num in changed:
            if num == 0 and count[num] >= 2:
                count[num] -= 2
                result.append(num)
            if num > 0 and count[num] and count[num * 2]:
                count[num] -= 1
                count[num * 2] -= 1
                result.append(num)
        return result if len(result) == len(changed) / 2 else []
