class Solution(object):
    def maxProduct(self, nums):
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
        target=float('-inf')
        total=nums[0]
        for i in range(len(nums)):
            
            for j in range(i+1,len(nums)):
                total*=nums[j]
                target=max(target,total)
        return target