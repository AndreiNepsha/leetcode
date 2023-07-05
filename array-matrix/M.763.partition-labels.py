class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        lp = [-1] * 26
        lc = [0] * 26
        cp = -1

        for char in s:
            c = ord(char) - 97
            if lp[c] == -1:
                cp += 1
                lp[c] = cp
            elif lp[c] != cp:
                cp = lp[c]
                for i in range(26):
                    if lp[i] != -1 and lp[i] > cp:
                        lp[i] = cp
            lc[c] += 1
        
        parts = [0] * (cp + 1)
        for i in range(26):
            if lp[i] > -1:
                parts[lp[i]] += lc[i]
        
        return parts
        