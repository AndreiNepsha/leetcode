class Solution:
    def _intToRoman(self, num: int) -> str:
        symb = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        roman = []
        i = 0
        while num > 0:
            digit = num % 10
            prefix = []
            if digit == 9:
                prefix = [symb[i], symb[i + 2]]
            elif digit == 4:
                prefix = [symb[i], symb[i + 1]]
            elif digit > 4:
                prefix = [symb[i + 1]] + [symb[i]] * (digit % 5)
            elif digit > 0:
                prefix = [symb[i]] * digit
            roman = prefix + roman
            num //= 10
            i += 2
        return "".join(roman)
    
    def intToRoman(self, num: int) -> str:
        bank = {1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}
        result = ''
        for i in bank:
            result += num // i * bank[i]
            num %= i
        return result


a = Solution().intToRoman(58)
assert "LVIII" == a, a
