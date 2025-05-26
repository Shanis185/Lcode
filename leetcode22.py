class Solution(object):
    def generateParenthesis(self, n):
        res=[]
        ans=[]
        def backtrack(openn,close):
            if len(ans)==2*n:
                res.append("".join(ans))
                return

            if openn<n:
                ans.append("(")
                backtrack(openn+1,close)
                ans.pop()
            if openn>close:
                ans.append(")")
                backtrack(openn,close+1)
                ans.pop()
        backtrack(0,0)
        return res