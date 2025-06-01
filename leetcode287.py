class Solution(object):
    def findDuplicate(self, nums):
       
        left = 1
        right = len(nums) - 1  

       
        while left<right:
            count=0
            mid=(left+right)//2

            for i in nums:
                if i<=mid:
                    count+=1
            if count>mid:
                right=mid
            else:
                left=mid+1
        return left
