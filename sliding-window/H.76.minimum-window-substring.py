class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_mask = [0] * 58
        for c in t:
            t_mask[ord(c) - 65] += 1
        
        c_mask = [0] * 58
        cur = 0

        l = 0
        k = ord(s[l]) - 65  
        window = ""
        for r, c in enumerate(s):
            i = ord(c) - 65
            c_mask[i] += 1

            if t_mask[i] > 0 and c_mask[i] <= t_mask[i]:
                cur += 1
            
            if cur == len(t):
                while t_mask[k] == 0 or c_mask[k] > t_mask[k]:
                    c_mask[k] -= 1
                    l += 1
                    k = ord(s[l]) - 65
                if not window or r - l < len(window) - 1:
                    window = s[l:r + 1]
        
        return window


a = Solution().minWindow(s = "ADOBECODEBANC", t = "ABC")
assert "BANC" == a, a
