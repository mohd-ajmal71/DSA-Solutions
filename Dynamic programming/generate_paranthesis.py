class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        result = ""
        op = n
        cl = n
        self.helper(op, cl, result, ans)
        return ans

    def helper(self, op, cl, result, ans):
        if op == 0 and cl == 0:
            ans.append(result)
            return

        if op != 0:
            result_1 = result
            result_1 += "("
            self.helper(op - 1, cl, result_1, ans)

        if cl > op:
            result_2 = result
            result_2 += ")"
            self.helper(op, cl - 1, result_2, ans)
