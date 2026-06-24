class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        count = k

        for ch in num:
            digit = int(ch)

            while count > 0 and stack and stack[-1] > digit:
                stack.pop()
                count -= 1

            stack.append(digit)

        while count > 0 and len(stack) != 0:
            stack.pop()
            count -= 1

        result = "".join(map(str, stack)).lstrip('0')

        return result if result else '0'
