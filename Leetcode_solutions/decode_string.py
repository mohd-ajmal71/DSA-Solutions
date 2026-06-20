class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current = ""
        num = 0

        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)

            elif ch == '[':
                stack.append(current)
                stack.append(num)
                current = ""
                num = 0

            elif ch == ']':
                k = stack.pop()
                prev = stack.pop()
                current = prev + current * k

            else:
                current += ch

        return current