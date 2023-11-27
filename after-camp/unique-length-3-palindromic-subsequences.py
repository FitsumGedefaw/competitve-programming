class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        pals = set()
        seen = defaultdict(list)
        for idx, ch in enumerate(s):
            if ch in seen:
                if idx > seen[ch][-1] + 1:
                    for i in range(seen[ch][-1] + 1, idx):
                        pals.add(ch + s[i] + ch)

                if len(seen[ch]) == 2 and (ch + ch + ch) not in pals:
                    pals.add(ch + ch + ch)

            seen[ch].append(idx)

        return len(pals)

                        


        