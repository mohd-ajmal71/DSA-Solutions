class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        max_sum1=nums[-1]*nums[-2]*nums[-3]
        max_sum2=nums[-1]*nums[0]*nums[1]

        if max_sum1>max_sum2:
            return max_sum1

        return max_sum2
        
        
        