class Solution(object):
    def splitArray(self, nums, k):
        if k>len(nums):
            return
        def helper(mid):
            count=1
            total=0
            for i in nums:
                if total+i>mid:
                    count+=1
                    total=i
                    if count>k:
                        return False
                    
                else:
                    total+=i
            return True
        




        left=max(nums)
        right=sum(nums)
        best_sub=0
        while left<=right:
            mid=(left+right)//2
            if helper(mid):
                best_sub=mid
                right=mid-1
            else:
                left=mid+1
        return best_sub
        