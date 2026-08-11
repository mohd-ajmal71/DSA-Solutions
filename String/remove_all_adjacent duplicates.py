class Solution:
    def removeDuplicates(self, s: str) -> str:
        ans=[]

        for i in range(len(s)):
            if ans and ans[-1]!=s[i]:
                ans.append(s[i])
            elif ans and ans[-1]==s[i]:
                ans.pop()
            else:
                ans.append(s[i])

        return "".join(ans)

        