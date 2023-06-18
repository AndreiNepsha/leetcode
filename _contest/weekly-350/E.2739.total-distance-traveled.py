class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        km = 0
        rem = 0
        while mainTank:
            km += mainTank * 10
            transfer = min(additionalTank, (mainTank + rem) // 5)
            rem = (mainTank + rem) % 5
            mainTank = transfer
            additionalTank -= transfer
        return km


assert 110 == Solution().distanceTraveled(mainTank = 9, additionalTank = 2)
assert 60 == Solution().distanceTraveled(mainTank = 5, additionalTank = 10)
assert 10 == Solution().distanceTraveled(mainTank = 1, additionalTank = 2)