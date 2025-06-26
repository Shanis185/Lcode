class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        ans=[]
        def backtrack(x):
            if x==len(s):
                res.append(ans[:])
                return

            for i in range(x+1,len(s)+1):
                substring=s[x:i]
                if substring==substring[::-1]:
                    ans.append(substring)
                    backtrack(i)
                    ans.pop()

        backtrack(0)
        return res   