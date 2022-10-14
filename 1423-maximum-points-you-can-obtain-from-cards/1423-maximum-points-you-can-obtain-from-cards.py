class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        for i in range(1, len(cardPoints)):
            cardPoints[i] += cardPoints[i-1]
        totalpts = cardPoints[-1]
        maxpt = 0
        l, r = 0, len(cardPoints)-k-1
        while r < len(cardPoints):
            windowSum = cardPoints[r] if l==0 else cardPoints[r]-cardPoints[l-1]
            maxpt = max(maxpt, totalpts-windowSum)
            l, r = l+1, r+1
        return maxpt
            