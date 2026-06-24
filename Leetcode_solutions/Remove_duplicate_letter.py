class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        fre_arr = [0] * 26
        seen = [False] * 26
        stack = []
        for ch in s:
            idx = ord(ch) - 97
            fre_arr[idx] += 1

        for i in range(len(s)):
            idx = ord(s[i]) - 97

            if seen[idx] == True:
                fre_arr[idx] -= 1
                continue
            fre_arr[idx] -= 1
            while stack and stack[-1] > s[i] and fre_arr[ord(stack[-1]) - 97] > 0:
                idx1 = ord(stack[-1]) - 97
                seen[idx1] = False
                stack.pop()

            stack.append(s[i])
            seen[idx] = True

        return "".join(stack)

