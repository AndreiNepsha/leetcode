class Solution:
    def checkStraightLine(self, coordinates: list[list[int]]) -> bool:
        left, right = (
            (coordinates[1], coordinates[0])
            if coordinates[1][0] < coordinates[0][0] 
            else (coordinates[0], coordinates[1])
        )
        if right[0] - left[0] == 0:
            for i in range(2, len(coordinates)):
                if coordinates[i][0] - left[0] != 0:
                    return False
            return True

        if right[1] - left[1] == 0:
            for i in range(2, len(coordinates)):
                if coordinates[i][1] - left[1] != 0:
                    return False
            return True

        k = (right[1] - left[1]) / (right[0] - left[0])
        b = left[1] - left[0] * k
        for i in range(2, len(coordinates)):
            if (
                coordinates[i][0] - left[0] == 0 or
                (coordinates[i][1] - left[1])
                / (coordinates[i][0] - left[0])
                != k
                or coordinates[i][1] - coordinates[i][0] * k != b
            ):
                return False
        return True


coordinates = [[1,-8],[2,-3],[1,2]]
assert not Solution().checkStraightLine(coordinates)

coordinates = [[-1, 1], [0, 0], [1, -1]]
assert Solution().checkStraightLine(coordinates)

coordinates = [[-1, 1], [1, -1], [0, 0]]
assert Solution().checkStraightLine(coordinates)

coordinates = [[0, 0], [0, 1], [0, -1]]
assert Solution().checkStraightLine(coordinates)

coordinates = [[0, 0], [1, 0], [-1, 0]]
assert Solution().checkStraightLine(coordinates)
