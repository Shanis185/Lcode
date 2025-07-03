from collections import defaultdict
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count=0
        prefix_sum=0
        prefix_count=defaultdict(int)
        prefix_count[0]=1
        for i in range(len(nums)):
            prefix_sum+=nums[i]
            count+=prefix_count[prefix_sum-goal]
            prefix_count[prefix_sum]+=1
        return count

        
