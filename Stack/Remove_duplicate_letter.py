class Solution:
    def removeDuplicateLetters(self, s: str) -> str:

        freq = [0] * 26
        seen = [False] * 26
        stack = []

        for ch in s:
            idx = ord(ch) - 97
            freq[idx] += 1

        for ch in s:
            idx = ord(ch) - 97
            freq[idx] -= 1

            if seen[idx]:
                continue

            while stack and stack[-1] > ch and freq[ord(stack[-1]) - 97] > 0:
                index = ord(stack[-1]) - 97
                seen[index] = False
                stack.pop()

            if seen[idx] == False:
                stack.append(ch)
                seen[idx] = True

        return "".join(stack)


