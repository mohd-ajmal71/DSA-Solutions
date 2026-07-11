class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        total = sum(candies)
        l, r = 1, (total // k)
        res = 0

        if total < k:
            return 0

        while l <= r:
            m = l + (r - l) // 2
            count = 0
            for c in candies:
                if c >= m:
                    count += c // m

                if count >= k:
                    break

            if count >= k:
                res = m
                l = m + 1
            else:
                r = m - 1

        return res

