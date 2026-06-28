class Solution:
    def customSortString(self, order: str, s: str) -> str:
        freq = [0] * 26
        ans = ""

        for ch in s:
            idx = ord(ch) - 97
            freq[idx] += 1

        for ch in order:
            if ch in s:
                idx = ord(ch) - 97
                if freq[idx] >= 0:
                    ans += freq[idx] * ch
                    freq[idx] = -1

        for i in range(len(freq)):
            ch = chr(i + 97)
            if freq[i] >= 0:
                ans += freq[i] * ch
        return ans


