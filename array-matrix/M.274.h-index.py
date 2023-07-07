class Solution:
    def hIndex(self, citations: list[int]) -> int:
        h = 0
        citations = sorted(citations)
        for i in range(len(citations) - 1, -1, -1):
            if citations[i] > h:
                h += 1
            else:
                break
        return h
