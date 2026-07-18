class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mini = min(nums)
        maxi = max(nums)
        count = 1
        gcd = 1
        while count <= mini:
            if mini % count == 0 and maxi % count == 0:
                gcd = count
            count += 1
        return gcd
