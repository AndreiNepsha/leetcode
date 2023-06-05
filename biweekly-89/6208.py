class Solution:
    def countTime(self, time: str) -> int:
        a = 1
        if time[0] == '?':
            if time[1] > "3" and time[1] != "?":
                a = 2
            else:
                a = 3
        if time[1] == '?':
            if time[0] == '?':
                a = 24
            elif time[0] == '2':
                a = 4
            else:
                a *= 10
        if time[3] == '?':
            a *= 6
        if time[4] == '?':
            a *= 10
        return a


time = "?5:00"
answer = Solution().countTime(time)
assert 2 == answer, answer

time = "0?:0?"
answer = Solution().countTime(time)
assert 100 == answer, answer

time = "??:00"
answer = Solution().countTime(time)
assert 24 == answer, answer

time = "2?:?0"
answer = Solution().countTime(time)
assert 24 == answer, answer

time = "??:??"
answer = Solution().countTime(time)
assert 1440 == answer, answer

time = "?5:??"
answer = Solution().countTime(time)
assert 120 == answer, answer

time = "2?:??"
answer = Solution().countTime(time)
assert 240 == answer, answer
