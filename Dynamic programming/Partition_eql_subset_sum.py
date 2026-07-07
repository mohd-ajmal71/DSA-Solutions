class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum = 0
        for num in nums:
            sum += num

        if sum % 2 != 0:
            return False

        m = len(nums)
        n = sum // 2
        mat = [[0 for i in range(n + 1)] for i in range(m + 1)]

        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0:
                    mat[i][j] = False
                if j == 0:
                    mat[i][j] = True

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if nums[i - 1] <= j:
                    mat[i][j] = mat[i - 1][j] or mat[i - 1][j - nums[i - 1]]
                else:
                    mat[i][j] = mat[i - 1][j]

        return mat[m][sum // 2]


