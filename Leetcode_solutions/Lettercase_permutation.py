class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = []

        def backtrack(i, path):
            if i == len(s):
                ans.append("".join(path))
                return

            if s[i].isdigit():
                path.append(s[i])
                backtrack(i + 1, path)
                path.pop()
            else:
                # lowercase
                path.append(s[i].lower())
                backtrack(i + 1, path)
                path.pop()

                # uppercase
                path.append(s[i].upper())
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return ans