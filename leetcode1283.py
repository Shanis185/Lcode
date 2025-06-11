class Solution(object):
    def smallestDivisor(self, nums, threshold):
        left=1
        right=max(nums)
        def divisor(mid):
            result=0
            for i in nums:
                result+=(i+mid-1)//mid
            return result<=threshold
        while left<right:
            mid=(left+right)//2

            if divisor(mid):
                right=mid
            else:
                left=mid+1
        return left
