class Solution(object):
    def permute(self, nums):
        res,ans=[],[]
        def backtrack():
            if len(ans)==len(nums):
                res.append(ans[:])
                return
            for x in nums:
                if x not in ans:
                    ans.append(x)
                    backtrack()
                    ans.pop()
        
        backtrack()
        return res

        