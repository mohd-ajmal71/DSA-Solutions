class Solution:
    def countAndSay(self, n: int) -> str:
        result = "1"
        count = 0
        for i in range(n - 1):
            ans = ""
            count = 0
            current = result[0]
            for ch in result:
                if current != ch:
                    ans = ans + str(count) + current
                    count = 1
                    current = ch
                else:
                    count += 1

            ans = ans + str(count) + ch
            result = ans
        return result
4