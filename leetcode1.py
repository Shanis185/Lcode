class Solution(object):
    def twoSum(self, nums, target):
        i=0
        n=len(nums)
        while i<n:
            for j in range(i+1,n):
                if nums[i]+nums[j]==target:
                    return [i,j]
            i+=1
        