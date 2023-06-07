class Solution:
    def findMedianSortedArrays(self, anums: list[int], bnums: list[int]) -> float:
        ln = len(anums) + len(bnums)
        median_position = ln // 2

        ap, bp = len(anums) // 2, len(bnums) // 2

        while ap + bp != median_position:
            if anums[ap] < bnums[bp]:
                
                ap = ap + (median_position - ap) // 2
            else:
                bp = bp + (median_position - bp) // 2

            return mid
        return -1


anums, bnums = [1,2], [3, 4]
r = Solution.findMedianSortedArrays(anums, bnums)
assert 2.5 == r, r

anums, bnums = [1,2], [4]
r = Solution.findMedianSortedArrays(anums, bnums)
assert 2 == r, r

anums, bnums = [1,2,3,4], [5]
r = Solution.findMedianSortedArrays(anums, bnums)
assert 3 == r, r

anums, bnums = [1,3,5], [2,4,6]
r = Solution.findMedianSortedArrays(anums, bnums)
assert 3.5 == r, r
