class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp=[[0]*(n+1) for _ in range(m+1)]
        counts=[]
        for s in strs:
            mcnt=s.count("0")
            ncnt=s.count("1")
            counts.append((mcnt,ncnt))
        for mcnt,ncnt in counts:
            for i in range(m,mcnt-1,-1):
                for j in range(n,ncnt-1,-1):
                    dp[i][j]=max(dp[i][j],dp[i-mcnt][j-ncnt]+1)
        return dp[m][n] 