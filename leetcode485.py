class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        maximum=0
        total=0
        
        for i in nums:
            if i==1:
                total+=1
                maximum=max(total,maximum)
            else:
                total=0
                maximum=max(total,maximum)
        return maximum

                