class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        component = [0] * n
        ans = [False] * len(queries)

        for i in range(1, n):
            diff = abs(nums[i] - nums[i - 1])
            if diff <= maxDiff:
                component[i] = component[i - 1]
            else:
                component[i] = i
        count = 0
        for i in queries:
            first = i[0]
            second = i[1]
            if component[first] == component[second]:
                ans[count] = True
            count += 1
        return ans


