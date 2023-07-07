class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        l, t, f, a = 0, 0, 0, 0
        for r in range(len(answerKey)):
            if answerKey[r] == "T":
                t += 1
            else:
                f += 1
            
            while min(t, f) > k:
                if answerKey[l] == "T":
                    t -= 1
                else:
                    f -= 1
                l += 1
            
            a = max(a, t + f)
        
        return a
