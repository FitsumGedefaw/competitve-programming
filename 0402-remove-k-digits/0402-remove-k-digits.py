class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        res = ""
        mst = deque()
        for i in range(len(num)):
            while k > 0 and mst and num[i] < mst[-1]:
                mst.pop()
                k -= 1
            mst.append(num[i])
        while len(mst) > k:
            res += mst.popleft()
        if res == "":
            return "0"
        while res[0] == "0" and len(res) > 1:
            res = res[1:]
        return res