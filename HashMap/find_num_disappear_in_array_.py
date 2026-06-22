class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        copy_num = nums[:]
        for val in nums:
            copy_num[val - 1] = -1

        for i in range(len(nums)):
            if copy_num[i] > -1:
                ans.append(i + 1)

        return ans




