class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        aboverow=[1]*n

        for i in range(m-1):
            currentrow=[1]*n
            for j in range(1,n):
                currentrow[j]=currentrow[j-1]+aboverow[j]
            aboverow=currentrow
        return aboverow[-1]