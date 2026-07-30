class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        result = 0
        for ch in s:
            result = result ^ ord(ch)

        for ch in t:
            result = result ^ ord(ch)

        return str(chr(result))
