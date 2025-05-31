class Solution(object):
    def moveZeroes(self, nums):
        n=len(nums)
        pos=0
        for i in range(n):
            if nums[i]!=0:
                nums[pos]=nums[i]
                pos+=1
        while pos<n:
            nums[pos]=0
            pos+=1
        
        