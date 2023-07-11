class Solution:
    def relocateMarbles(self, nums: list[int], moveFrom: list[int], moveTo: list[int]) -> list[int]:
        positions = set(nums)
        for i in range(len(moveFrom)):
            positions.remove(moveFrom[i])
            positions.add(moveTo[i])
        return sorted(positions)



a = Solution().relocateMarbles(nums = [1,6,7,8], moveFrom = [1,7,2], moveTo = [2,9,5])
assert [5,6,8,9] == a, a

a = Solution().relocateMarbles(nums = [1,1,3,3], moveFrom = [1,3], moveTo = [2,2])
assert [2] == a, a
