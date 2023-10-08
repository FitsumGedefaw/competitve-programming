class Solution:
    def longestWord(self, words: List[str]) -> str:
        words=sorted(words)
        r=''
        ws=set()
        for i in words:
            p=len(i)
            if p==1 or i[:-1] in ws:
                if p>len(r):
                    r=i
                ws.add(i)
        return r