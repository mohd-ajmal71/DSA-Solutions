class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            if count == 0:
                current = num

            if num == current:
                count += 1

            else:
                count -= 1

        return current




