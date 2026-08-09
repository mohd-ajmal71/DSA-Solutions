class Solution:
    def findLHS(self, nums: List[int]) -> int:
        count=Counter(nums)
        res=0
        for i in count:
            num=i+1
            if num in count:
                res=max(res,count[i]+count[i+1])
        return res
        