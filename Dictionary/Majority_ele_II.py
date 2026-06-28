class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums) // 3
        freq = {}
        ans = []
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        for k, v in freq.items():
            if v > n:
                ans.append(k)
        return ans


