class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_freq = [0] * 26

        for ch in s:
            idx = ord(ch) - 97
            char_freq[idx] += 1

        count = 0
        for ch in s:
            idx = ord(ch) - 97
            if char_freq[idx] == 1:
                return count
            count += 1

        return -1




