class Solution(object):
    def longestConsecutive(self, nums):
        if not nums:
            return 0
        n=len(nums)
        nums=set(nums)
        max_length=1
        for num in nums:
            if num-1 not in nums:
                curr_num=num
                curr_length=1
                while curr_num+1 in nums:
                    curr_num+=1
                    curr_length+=1
                max_length=max(curr_length,max_length)
        return max_length
                 

