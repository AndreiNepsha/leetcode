from collections import deque


class Solution:
    def floodFill(
        self, image: list[list[int]], sr: int, sc: int, color: int
    ) -> list[list[int]]:
        initial_color = image[sr][sc]
        if initial_color == color:
            return image

        rows = len(image)
        columns = len(image[0])

        queue = deque()
        queue.append((sr, sc))

        while len(queue) > 0:
            sr, sc = queue.popleft()
            image[sr][sc] = color
            if sr + 1 < rows and image[sr + 1][sc] == initial_color:
                queue.append((sr + 1, sc))
            if sr - 1 >= 0 and image[sr - 1][sc] == initial_color:
                queue.append((sr - 1, sc))
            if sc + 1 < columns and image[sr][sc + 1] == initial_color:
                queue.append((sr, sc + 1))
            if sc - 1 >= 0 and image[sr][sc - 1] == initial_color:
                queue.append((sr, sc - 1))

        return image


assert [[2, 2, 2], [2, 2, 0], [2, 0, 1]] == Solution().floodFill(
    [[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2
)
