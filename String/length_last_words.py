class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        ans = ""

        for ch in s[::-1]:
            if ch != " ":
                ans = ch + ans
            else:
                break
        return len(ans)
