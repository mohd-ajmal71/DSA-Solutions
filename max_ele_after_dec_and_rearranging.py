class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        prev = 0

        for num in arr:
            prev = min(prev + 1, num)
        return prev