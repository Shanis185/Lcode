class Solution(object):
    def subarraySum(self, nums, k):
        current_sum=0
        prefix_sum=defaultdict(int)
        prefix_sum[0]=1
        count=0

        for i in nums:
            current_sum=current_sum+i

            if current_sum-k  in prefix_sum:
                count+=prefix_sum[current_sum-k]
            prefix_sum[current_sum]+=1
        return count