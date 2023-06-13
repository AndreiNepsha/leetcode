class Solution:
    def romanToInt(self, s: str) -> int:
        ls = len(s)
        se = ls - 1
        bank = {1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}
        result = 0
        k = 0
        for i, r in bank.items():
            lr = len(r)
            while k < ls and s[k] == r[0] and (lr == 1 or k < se and s[k + 1] == r[1]):
                result += i
                k += lr
        return result

s = "III"
assert 3 == Solution().romanToInt(s)
