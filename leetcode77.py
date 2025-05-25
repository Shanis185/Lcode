class Solution(object):
    def combine(self, n, k):
        res,ans=[],[]
        def backtrack(x):
            if len(ans)==k:
                res.append(ans[:])
                return
            for i in range(x,n+1):
                ans.append(i)
                backtrack(i+1)
                ans.pop()
        backtrack(1)
        return res
        