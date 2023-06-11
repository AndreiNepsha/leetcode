# TODO solve
# https://leetcode.com/problems/movement-of-robots/

class Solution:
    def sumDistance(self, nums: list[int], s: str, d: int) -> int:
        MD = 10**9 + 7
        distance = 0
        ln = len(nums)
        robots = list(map(list, sorted(zip(nums, s, nums), key=lambda x: x[0])))
        left, right = 0, ln - 1
        while left < right:
            print(robots)
            while left < ln - 1 and robots[left][1] == "L":
                distance = (distance + abs(robots[left][2] - robots[left][0]) + d) % MD
                left += 1
            while left <= right and robots[right][1] == "R":
                distance = (distance + abs(robots[left][2] - robots[left][0]) + d) % MD
                right -= 1
            next_col = d
            for i in range(left, right):
                if robots[i][1] == "R" and robots[i + 1][1] == "L" and robots[i][0] != robots[i + 1][0]:
                    next_col = min(next_col, abs(robots[i][0] - robots[i + 1][0]) // 2)
            i = left
            while i <= right:
                if i < right and robots[i][1] == "R" and robots[i + 1][1] == "L" and abs(robots[i][0] - robots[i + 1][0]) // 2 == next_col:
                    robots[i][0] = robots[i][0] + next_col if robots[i][1] == "R" else robots[i][0] - next_col
                    robots[i + 1][0] = robots[i + 1][0] + next_col if robots[i + 1][1] == "R" else robots[i + 1][0] - next_col
                    robots[i][1] = "L" if robots[i][1] == "R" else "R"
                    robots[i + 1][1] = "L" if robots[i + 1][1] == "R" else "R"
                    i += 2
                else:
                    robots[i][0] = robots[i][0] + next_col if robots[i][1] == "R" else robots[i][0] - next_col
                    i += 1
            d -= next_col
        print(robots)
        return distance

nums = [-2,0,2]
s = "RLL"
d = 3
a = Solution().sumDistance(nums, s, d)
assert 8 == a, a
