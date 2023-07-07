from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        letters_count = defaultdict(int)
        max_letters = 0
        other_letters = 0
        l = 0

        for r in range(len(s)):
            letters_count[s[r]] += 1
            if letters_count[s[r]] > max_letters:
                max_letters = letters_count[s[r]]
            else:
                other_letters += 1
            
            if other_letters > k:
                letters_count[s[l]] -= 1
                other_letters -= 1
                l += 1

        return max_letters + other_letters


a = Solution().characterReplacement(s = "ABAB", k = 2)
assert 4 == a, a

a = Solution().characterReplacement(s = "AABABBA", k = 1)
assert 4 == a, a
