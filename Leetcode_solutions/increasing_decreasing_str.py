class Solution:
    def sortString(self, s: str) -> str:
        count = len(s)
        ans = ""
        freq = [0] * 26
        for ch in s:
            idx = ord(ch) - 97
            freq[idx] += 1

        while count > 0:
            for i in range(26):
                if freq[i] > 0 and count > 0:
                    ch = chr(97 + i)
                    ans += ch
                    freq[i] -= 1
                    count -= 1

            for i in range(25, -1, -1):
                if freq[i] > 0 and count > 0:
                    ch = chr(97 + i)
                    ans += ch
                    freq[i] -= 1
                    count -= 1

        return ans




