from collections import Counter


def swap(a, l, r):
    tmp = a[l]
    a[l] = a[r]
    a[r] = tmp


class Solution:
    def reorganizeString(self, s: str) -> str:
        pk = sorted(
            [[l, c] for l, c in Counter(s).items()], key=lambda x: x[1], reverse=True
        )
        lpi = len(pk) - 1
        r = []
        take = 0
        while lpi > 0:
            pk[take][1] -= 1
            r.append(pk[take][0])
            i = take + 1
            while i <= lpi and pk[take][1] < pk[i][1]:
                i += 1
            if pk[take][1] == 0:
                lpi -= 1
            if i == 1:
                take = 1
            else:
                swap(pk, i - 1, take)
                take = 0
            # print(r)
            # print(pk)
        if lpi == 0:
            if pk[0][1] > 1:
                return ""
            else:
                r.append(pk[0][0])
        return "".join(r)


s = "wawwivhwfrgontvvfggh"
a = Solution().reorganizeString(s)
assert "wvwgwghvfvfnoriawght" == a, a

s = "aaabc"
a = Solution().reorganizeString(s)
assert "abaca" == a, a

s = "aab"
a = Solution().reorganizeString(s)
assert "aba" == a, a

s = "aaabdddd"
a = Solution().reorganizeString(s)
assert "dabdadad" == a, a
