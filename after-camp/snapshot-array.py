class SnapshotArray:

    def __init__(self, length: int):
        self.arr = {idx: [(-1, 0)] for idx in range(length)}
        self.numOfSwaps = 0
        
    def set(self, index: int, val: int) -> None:
        next_snap_id = self.numOfSwaps
        self.arr[index].append((next_snap_id, val))

    def snap(self) -> int:
        self.numOfSwaps += 1
        return self.numOfSwaps - 1
        
    def get(self, index: int, snap_id: int) -> int:
        left, right = 0, len(self.arr[index]) - 1
        while left < right:
            mid = ceil(left + (right - left) / 2)
            if self.arr[index][mid][0] <= snap_id:
                left = mid
            else:
                right = mid - 1
        return self.arr[index][left][1]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)