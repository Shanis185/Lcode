class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums)%k!=0:
            return False
        nums.sort(reverse=True)
        target=sum(nums)/k
        used=[False]*len(nums)
        
        def backtrack(i,k,subsum):
            if k==0:
                return True
            if subsum==target:
                return backtrack(0,k-1,0)
            
            for j in range(i,len(nums)):
                if j>0 and not used[j-1] and nums[j]==nums[j-1]:
                    continue #this line is only for time efficiency
                if used[j] or subsum+nums[j]>target:
                    continue
                used[j]=True
                if backtrack(j,k,subsum+nums[j]):
                    return True
                used[j]=False
            return False
        return backtrack(0,k,0)