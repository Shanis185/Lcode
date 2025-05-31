class Solution(object):
    def missingNumber(self, nums):
        n=len(nums)
        j=[]
        for i in range(n+1):
            j.append(i)
        for i in j:
            if i not in nums:
                return i
        