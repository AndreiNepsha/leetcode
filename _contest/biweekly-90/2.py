from typing import List


class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        n = len(queries[0])
        res = []
        for q in queries:
            for d in dictionary:
                ers = 0
                for i in range(n):
                    if q[i] != d[i]:
                        ers += 1
                        if ers > 2:
                            break
                if ers <= 2:
                    res.append(q)
                    break
        return res

queries = ["word", "note", "ants", "wood"]
dictionary = ["wood", "joke", "moat"]
a = Solution().twoEditWords(queries, dictionary)
assert ["word", "note", "wood"] == a, a
