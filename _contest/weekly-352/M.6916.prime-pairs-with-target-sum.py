class Solution:
    def findPrimePairs(self, n: int) -> list[list[int]]:
        def get_primes(n):
            sieve = [True] * n
            for i in range(3, int(n ** 0.5)+1, 2):
                if sieve[i]:
                    sieve[i * i::2 * i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
            return [2] + [i for i in range(3, n, 2) if sieve[i]]
        
        primes = get_primes(n)

        def search(nums: list[int], target: int, left: int) -> int:
            ln = len(nums)
            right = ln - 1

            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    return mid
            return -1

        pairs = []
        
        for i, p in enumerate(primes):
            if (j := search(primes, n - p, i)) >= 0:
                pairs.append([primes[i], primes[j]])
        
        return pairs

Solution().findPrimePairs(9999)