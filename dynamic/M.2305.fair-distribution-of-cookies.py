from heapq import heappop, heappush


class Solution:
    def distributeCookies(self, cookies: list[int], k: int) -> int:
        li = len(cookies)

        heap = [0] * k
        cookies.sort(reverse=True)
        for c in cookies:
            heappush(heap, heappop(heap) + c)
        fair = max(heap)

        child_cookies = [0] * k
        childs = {i for i in range(k)}
        def dfs(i):
            nonlocal fair
            if i == li:
                fair = min(fair, max(child_cookies))
                return
            for child in childs:
                if child_cookies[child] + cookies[i] < fair:
                    child_cookies[child] = child_cookies[child] + cookies[i]
                    dfs(i + 1)
                    child_cookies[child] = child_cookies[child] - cookies[i]
        dfs(0)
        
        return fair


a = Solution().distributeCookies(cookies = [8,15,10,20,8], k = 2)
assert 31 == a, a

a = Solution().distributeCookies(cookies = [6,1,3,2,2,4,1,2], k = 3)
assert 7 == a, a

a = Solution().distributeCookies(cookies = [75027,58436,95472,89426,10786,32325,99823,33237], k = 5)
assert 107352 == a, a