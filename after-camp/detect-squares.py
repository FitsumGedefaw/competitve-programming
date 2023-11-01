class DetectSquares:

    def __init__(self):
        self.ptsCt = defaultdict(int)
        self.xVals = defaultdict(list)

    def add(self, point: List[int]) -> None:
        self.ptsCt[(point[0], point[1])] += 1
        self.xVals[point[0]].append(point[1])

    def count(self, point: List[int]) -> int:
        ans = 0
        for y in self.xVals[point[0]]:
            if y != point[1]:
                sideLen = abs(y - point[1])
                ans += self.ptsCt[(point[0]+sideLen, y)] * self.ptsCt[(point[0]+sideLen, point[1])]
                ans += self.ptsCt[(point[0]-sideLen, y)] * self.ptsCt[(point[0]-sideLen, point[1])]
        return ans


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)