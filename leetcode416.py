class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total=sum(nums)
        if total%2==1:
            return False
        target=total//2

        dp=[False]*(target+1)
        dp[0]=True
        for i in nums:
            for j in range(len(dp)-1,i-1,-1):
                if dp[j]:
                    continue
                if dp[j-i]:
                    dp[j]=True
                if dp[-1]:
                    return True
        return  False