class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        size = len(s)
        ans = {}
        left = 0
        right = 0
        count = 0
        while right < len(s):
            if s[right] in ans:
                ans[s[right]] += 1
            else:
                ans[s[right]] = 1
            right += 1

            while 'a' in ans and 'b' in ans and 'c' in ans:
                count += size - right + 1
                if s[left] in ans and ans[s[left]] > 1:
                    ans[s[left]] -= 1
                else:
                    del ans[s[left]]

                left += 1
        return count



