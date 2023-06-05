

from collections import Counter
from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        if n <= 10:
            return []
        c = Counter()
        for i in range(n - 10):
            c.update([s[i : i + 10]])
        return [
            k for k, v in c.items() if v > 1
        ]

s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
a = Solution().findRepeatedDnaSequences(s)
assert ["AAAAACCCCC","CCCCCAAAAA"] == a, a
