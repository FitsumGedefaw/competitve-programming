class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        count = defaultdict(int)
        for word in words:
            count[word] += 1
        
        ans = 0
        F = 0

        for word in words:
            if count[word] > 0:
                if word[0] == word[1]:
                    if count[word] % 2 == 0:
                        ans += (count[word] * 2)
                    else:
                        F = 1
                        ans += ((count[word] - 1) * 2)
                    count[word] = 0
                else:
                    wordRev = word[::-1]
                    if count[wordRev] > 0:
                        if count[word] <= count[wordRev]:
                            ans += (count[word] * 4)
                            count[word] = 0
                            count[wordRev] -= count[word]
                        else:
                            ans += (count[wordRev] * 4)
                            count[wordRev] = 0
                            count[word] -= count[wordRev]

        return ans + (2 if F == 1 else 0)

                    
        

        