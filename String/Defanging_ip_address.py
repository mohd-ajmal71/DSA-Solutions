class Solution:
    def defangIPaddr(self, address: str) -> str:
        ans = ""
        for ch in address:
            if ch == '.':
                ans += "[.]"
                continue
            ans += ch
        return ans


