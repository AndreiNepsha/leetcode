class Solution:
    def smallestString(self, s: str) -> str:
        ls = len(s)
        i = 0
        s = list(s)
        while i < ls and s[i] == 'a':
            i += 1
        if i == ls:
            return "".join(['a'] * (ls - 1) + ['z'])
        while i < ls and s[i] != 'a':
            s[i] = chr(ord(s[i]) - 1)
            i += 1
        return "".join(s)
    