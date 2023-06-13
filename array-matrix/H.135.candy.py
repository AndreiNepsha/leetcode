class Solution:
    def candy(self, ratings: list[int]) -> int:
        ln = len(ratings)
        candies = 1
        extremum = 1
        extremum_i = 0
        for i in range(1, ln):
            if ratings[i] > ratings[i - 1]:
                if i - extremum_i > 1:
                    extremum = 1
                extremum += 1
                extremum_i = i
                candies += extremum
            elif ratings[i] == ratings[i - 1]:
                extremum = 1
                extremum_i = i
                candies += extremum
            else:
                if i - extremum_i >= extremum:
                    candies += 1
                candies += i - extremum_i
        return candies


ratings = [1,3,2,2,1]  # 1, 2, 1, 2, 1
a = Solution().candy(ratings)
assert 7 == a, a

ratings = [1,0,2]
a = Solution().candy(ratings)
assert 5 == a, a