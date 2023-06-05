class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n3 = len(s3)
        n2 = len(s2)
        n1 = len(s1)
        if n1 + n2 != n3:
            return False

        i1_s, i2_s, i3_s = 0, 0, 0

        def _check(i, s, i3, n):
            while i < n and i3 < n3:
                if s[i] != s3[i3]:
                    break
                i += 1
                i3 += 1
            return i, i3

        reverse = False
        queue = []

        while i3_s < n3:
            if s1[i1_s] == s2[i2_s]:
                queue.append((i1_s, i2_s, i3_s))
            if reverse:
                i1, i3 = _check(i1_s, s1, i3_s, n1)
                i2, i3 = _check(i2_s, s2, i3, n2)
            else:
                i2, i3 = _check(i2_s, s2, i3_s, n2)
                i1, i3 = _check(i1_s, s1, i3, n1)
            if i1 + i2 == n3:
                return True
            if i1 == i1_s or i2 == i2_s:
                if reverse:
                    if queue:
                        i1_s, i2_s, i3_s = queue.pop()
                        continue
                    return False
                else:
                    reverse = True
                    queue.pop()
                    continue
            reverse = False
            i1_s = i1
            i2_s = i2
            i3_s = i3
        return True


s1 = "caba"
s2 = "abr"
s3 = "cabraba"
a = Solution().isInterleave(s1, s2, s3)
assert a

s1 = "aabc"
s2 = "abad"
s3 = "aabcabad"
a = Solution().isInterleave(s1, s2, s3)
assert a

s1 = "a"
s2 = "b"
s3 = "a"
a = Solution().isInterleave(s1, s2, s3)
assert not a

s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
a = Solution().isInterleave(s1, s2, s3)
assert a

s1 = "ab"
s2 = "bc"
s3 = "babc"
a = Solution().isInterleave(s1, s2, s3)
assert a

s1 = "aab"
s2 = "aac"
s3 = "aacaab"
a = Solution().isInterleave(s1, s2, s3)
assert a

s1 = "a"
s2 = ""
s3 = "c"
a = Solution().isInterleave(s1, s2, s3)
assert not a

