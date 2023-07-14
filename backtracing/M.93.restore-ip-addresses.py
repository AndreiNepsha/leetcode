class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        n = len(s)
        res = []
        dots = []

        ip_str_buf = [None] * (len(s) + 3)
        def make_ip_str():
            d = 0
            j = 0
            for i, c in enumerate(s):
                if d < 3 and i == dots[d]:
                    ip_str_buf[j] = "."
                    j += 1
                    d += 1
                ip_str_buf[j] = c
                j += 1
            return "".join(ip_str_buf)


        def backtrace(r):
            if len(dots) == 3 or r == n:
                if r < n and (s[r] != "0" or r == n - 1) and int(s[r:]) <= 255:
                    res.append(make_ip_str())
                return

            if s[r] == "0":
                dots.append(r + 1)
                backtrace(r + 1)
                dots.pop()
            else:
                for i in range(1, min(4, n - r)):
                    new_r = r + i
                    if int(s[r:new_r]) <= 255:
                        dots.append(new_r)
                        backtrace(new_r)
                        dots.pop()
        
        backtrace(0)

        return res


a = Solution().restoreIpAddresses(s = "25525511135")
assert ["255.255.11.135","255.255.111.35"] == a, a

a = Solution().restoreIpAddresses(s = "0000")
assert ["0.0.0.0"] == a, a

a = Solution().restoreIpAddresses(s = "1111")
assert ["0.0.0.0"] == a, a

a = Solution().restoreIpAddresses(s = "101023")
assert ["0.0.0.0"] == a, a
