# TODO improve solution
# https://leetcode.com/problems/snapshot-array/solutions/

class SnapshotArray:
    def __init__(self, length: int):
        self.snaps = [dict()]
        self.ls = 0

    def set(self, index: int, val: int) -> None:
        self.snaps[self.ls][index] = val

    def snap(self) -> int:
        self.snaps.append(dict())
        self.ls += 1
        return self.ls - 1

    def get(self, index: int, snap_id: int) -> int:
        return self.snaps[snap_id].get(index, 0)


for i in range(5, -1 -1):
    print(i)

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)