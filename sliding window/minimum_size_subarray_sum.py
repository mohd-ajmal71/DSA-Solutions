class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        window_size = 1
        subarray = 0
        right = 0
        minimum = 10 ** 18

        for value in nums:
            subarray += value
            right += 1

            while subarray >= target:
                window_size = right - left
                subarray -= nums[left]
                left += 1
                if minimum > window_size:
                    minimum = window_size

        return 0 if minimum == 10 ** 18 else minimum







