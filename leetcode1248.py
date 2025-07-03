from collections import defaultdict
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        count=0
        prefix_sum=0
        prefix_count=defaultdict(int)
        prefix_count[0]=1
        for i in range(len(nums)):
            if nums[i]%2==1:
                nums[i]=1
            else:
                nums[i]=0

        for i in nums:
            prefix_sum+=i
            count+=prefix_count[prefix_sum-k]
            prefix_count[prefix_sum]+=1
        return count
