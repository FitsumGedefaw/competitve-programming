class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) <= 10:
            return []

        seen = {s[ : 10] : 0}

        ans = []
        left = 0
        right = 10

        while right < len(s):
            text = s[left + 1 : right + 1]
            if text in seen:
                if seen[text] == 0:
                    ans.append(text)
                    seen[text] = 1
            else:
                seen[text] = 0

            left, right = left + 1, right + 1
        
        return ans



        