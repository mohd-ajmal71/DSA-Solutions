class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        freq = {}
        ans = []
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        for k, f in freq.items():
            if f == 2:
                ans.append(k)
        return ans
