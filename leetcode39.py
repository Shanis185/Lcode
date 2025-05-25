class Solution(object):
    def combinationSum(self, candidates, target):
        res,ans=[],[]
        def backtrack(x,total):
            if total==target:
                res.append(ans[:])
                return
            if total>target:
                return
            
            for i in range(x,len(candidates)):
                ans.append(candidates[i])
                backtrack(i,total+candidates[i])
                ans.pop()
        backtrack(0,0)
        return res
        