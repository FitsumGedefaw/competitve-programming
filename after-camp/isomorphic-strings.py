class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        rep = {}
        takenLetters = set()

        for i in range(len(s)):
            if s[i] not in rep:
                if t[i] not in takenLetters:
                    rep[s[i]] = t[i]
                    takenLetters.add(t[i])
                else:
                    return False
            else:
                if rep[s[i]] != t[i]:
                    return False

        return True
        