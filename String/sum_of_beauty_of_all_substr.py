class Solution:
    def beautySum(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            freq = [0] * 26
            for j in range(i, len(s)):
                idx = ord(s[j]) - 97
                freq[idx] += 1
                maxi = max(freq)
                mini = min(x for x in freq if x > 0)
                ans += maxi - mini
        return ans

