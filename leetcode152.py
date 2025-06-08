class Solution(object):
    def maxProduct(self, nums):
        curr_max=curr_min=result=nums[0]

        for i in nums[1:]:
            if i<0:
                curr_max,curr_min=curr_min,curr_max
            curr_max=max(i,curr_max*i)
            curr_min=min(i,curr_min*i)
            result=max(result,curr_max)
        return result
        