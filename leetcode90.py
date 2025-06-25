class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        ans=[]
        nums.sort()
        def dfs(x):
            res.append(ans[:])

            for i in range(x,len(nums)):
                if i>x and nums[i]==nums[i-1]:
                    continue
                ans.append(nums[i])
                dfs(i+1)
                ans.pop()

        dfs(0)
        return res

        