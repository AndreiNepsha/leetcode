class Solution:
    # clearer solution
    def isMatch(self, s: str, p: str) -> bool:
        n, m = len(s), len(p)
        i, j = 0, 0
        star, match = -1, 0
        while i < n:
            if j < m and (p[j] == '?' or p[j] == s[i]):
                i += 1
                j += 1
            elif j < m and p[j] == '*':
                star = j
                match = i
                j += 1
            elif star != -1:
                j = star + 1
                match += 1
                i = match
            else:
                return False
        while j < m and p[j] == '*':
            j += 1
        return j == m
    
    # second try
    def _isMatch(self, s: str, p: str) -> bool:
        pn, sn = len(p), len(s)
        ps, ss, si = 0, 0, 0
        begin_check = True
        while ps <= pn and si <= sn:
            pi = ps
            si = ss
            while pi < pn and si < sn and (p[pi] == "?" or p[pi] == s[si]):
                si += 1
                pi += 1
            if pi < pn and p[pi] != "*":
                if begin_check:
                    return False
                ss += 1
            while pi < pn and p[pi] == "*":
                ss = si
                pi += 1
                ps = pi
                begin_check = False
            if pi == pn or si == sn:
                if si != sn:
                    si = sn - 1
                    pi = pn - 1
                    while si >= 0 and pi >= 0 and (s[si] == p[pi] or p[pi] == "?"):
                        si -= 1
                        pi -= 1
                    return pi >= 0 and p[pi] == "*" and len([c for c in p if c != "*"]) <= sn
                return pi == pn and (si == sn or p and p[-1] == "*")
        return False
    
        # def check_window(i, w):
        #     window_n = len(w)
        #     for k in range(window_n):
        #         if w[k] != "?" and w[k] != s[i + k]:
        #             break
        #         elif k == window_n - 1:
        #             return True
        #     return window_n == 0

        # windows = p.split("*")
        # sn, windows_n = len(s), len(windows)

        # if windows_n == 1:
        #     return len(p) == sn and check_window(0, p)

        # l, r = 0, sn
        # start_p, end_p = windows[0], windows[-1]
        # spn, epn = len(start_p), len(end_p)
        # if spn:
        #     if spn > sn or not check_window(0, start_p):
        #         return False
        #     l = spn
        # if epn:
        #     if spn > sn - epn or not check_window(sn - epn, end_p):
        #         return False
        #     r = sn - epn

        # if windows_n == 2:
        #     return True

        # for wi in range(1, windows_n - 1):
        #     window_n = len(windows[wi])

        #     match = False
        #     while not match and l + window_n <= r:
        #         if check_window(l, windows[wi]):
        #             l += window_n
        #             match = True
        #         else:
        #             l += 1
        #             if l + window_n > r:
        #                 return False
        #     if match and wi == windows_n -2:
        #         return True
        # return False

assert not Solution().isMatch("aaab", "b**")
assert Solution().isMatch("aaaa", "***a")
assert not Solution().isMatch("babaaababaabababbbbbbaabaabbabababbaababbaaabbbaaab", "***bba**a*bbba**aab**b")
assert Solution().isMatch("adceb", "*a*b")
assert not Solution().isMatch("aaaaaa", "?*?b**")
assert Solution().isMatch("aaabbaabbaab", "*aabbaa*a*")
assert Solution().isMatch("ho", "ho**")
assert Solution().isMatch("ho", "**ho")
assert not Solution().isMatch("", "ab*")
assert Solution().isMatch("ab", "*?*?*")
assert Solution().isMatch("", "****")
assert Solution().isMatch("", "")
assert Solution().isMatch("abcabczzzde", "*abc???de*")
assert Solution().isMatch("alkfd", "al*k?d")