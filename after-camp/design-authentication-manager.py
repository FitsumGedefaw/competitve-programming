class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.timeToLive = timeToLive
        self.tokenExpiryTime = {}
        

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.tokenExpiryTime[tokenId] = currentTime + self.timeToLive

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.tokenExpiryTime and self.tokenExpiryTime[tokenId] > currentTime:
            self.tokenExpiryTime[tokenId] = currentTime + self.timeToLive
        
    def countUnexpiredTokens(self, currentTime: int) -> int:
        #T.C: O(n + logn)
        
        expiryTimes = sorted(self.tokenExpiryTime.values())
        #find the smallest expiry time that is greater than the current time
        left, right = 0, len(expiryTimes)
        while left < right:
            mid = left + (right - left) // 2
            if expiryTimes[mid] <= currentTime:
                left = mid + 1
            else:
                right = mid
        
        return len(expiryTimes) - right

        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)