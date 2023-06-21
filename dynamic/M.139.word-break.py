class Solution:
    def _wordBreak(self, s: str, wordDict: list[str]) -> bool:
        ls = len(s)

        def startswith(i, w):
            for c in w:
                if i >= ls or c != s[i]:
                    return False
                i += 1
            return True

        mem = [True] * ls

        def search(i):
            if ls == i:
                return True

            if not mem[i]:
                return False
            
            for w in wordDict:
                if startswith(i, w):
                    if search(i + len(w)):
                        return True
            
            mem[i] = False
            return False
        
        return search(0)

    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        wordSet = set(wordDict)
        wordLengths = set([len(w) for w in wordDict])
        T = [False] * len(s)
        for i in range(len(s)):
            for wl in wordLengths:
                left = i - wl + 1
                if left < 0:
                    continue
                if s[left:i+1] in wordSet and (left == 0 or T[left - 1]):
                    T[i] = True
                    break
        return T[len(s) - 1]


assert Solution().wordBreak(s = "leetcode", wordDict = ["leet","code"])
assert Solution().wordBreak(s = "applepenapple", wordDict = ["apple","pen"])
assert not Solution().wordBreak(s = "catsandog", wordDict = ["cats","dog","sand","and","cat"])
