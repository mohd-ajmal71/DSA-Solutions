class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}
        ans = ""

        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1

        sorted_freq = dict(sorted(freq.items(), reverse=True, key=lambda x: x[1]))

        for k, v in sorted_freq.items():
            ans += k * v
        return ans

