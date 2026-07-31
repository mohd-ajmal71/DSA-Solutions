class Solution:
    def compress(self, chars: List[str]) -> int:
        ans = ""
        count = 1
        for i in range(len(chars) - 1):
            if chars[i] == chars[i + 1]:
                count += 1
            else:
                if count != 1:
                    ans += chars[i] + str(count)
                    count = 1
                else:
                    ans += chars[i]

        if count != 1:
            ans += chars[len(chars) - 1] + str(count)
            count = 1
        else:
            ans += chars[len(chars) - 1]

        z = 0
        for i in ans:
            chars[z] = i
            z += 1
        return len(ans)



