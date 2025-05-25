class Solution(object):
    def subsets(self, nums):
        result=[]
        subset=[]
        n=len(nums)
        def dfs(i):
            if i>=n:
                result.append(subset[:])
                return 
            subset.append(nums[i])
            dfs(i+1)
            subset.pop()
            dfs(i+1)
        dfs(0)
        return result
        