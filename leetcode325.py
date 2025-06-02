class Solution:
    def longestSubarray(self, nums, k):
        max_length=0
        prefix_sum=0
        prefix_sum_={0:-1}

        for i,num in enumerate(nums):
                prefix_sum+=num
                if (prefix_sum-k) in prefix_sum_:
                    length=i-prefix_sum_[prefix_sum-k]
                    max_length=max(max_length,length)

                if (prefix_sum-k) not in prefix_sum_:
                    prefix_sum_[prefix_sum]=i
        return max_length