class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        ln = len(letters)
        left, right = 0, ln - 1

        if target < letters[left] or target >= letters[right]:
            return letters[left]

        while left <= right:
            mid = left + (right - left) // 2
            if letters[mid] <= target:
                left = mid + 1
            elif letters[mid] > target:
                right = mid - 1
        return letters[left]


letters = ["c","f","j"]
target = "a"
a = Solution().nextGreatestLetter(letters, target)
assert "c" == a, a

letters = ["c","f","j"]
target = "d"
a = Solution().nextGreatestLetter(letters, target)
assert "f" == a, a

letters = ["e","e","g","g"]
target = "g"
a = Solution().nextGreatestLetter(letters, target)
assert "e" == a, a

letters = ["e","e","f","g","g"]
target = "e"
a = Solution().nextGreatestLetter(letters, target)
assert "f" == a, a
