class Solution:
    def get_ord(self, s):
        return ord(s) - ord("a")

    def get_d(self, word):
        return [
            self.get_ord(word[i]) - self.get_ord(word[i - 1])
            for i in range(1, len(word))
        ]

    def oddString(self, words: list[str]) -> str:
        triple = [self.get_d(words[i]) for i in range(3)]
        if triple[0] == triple[1] and triple[1] == triple[2]:
            for i in range(3, len(words)):
                if self.get_d(words[i]) != triple[0]:
                    return words[i]
        else:
            if triple[0] == triple[1]:
                return words[2]
            if triple[1] == triple[2]:
                return words[0]
            if triple[0] == triple[2]:
                return words[1]


a = Solution().oddString(["adc", "wzy", "abc"])
assert "abc" == a, a
