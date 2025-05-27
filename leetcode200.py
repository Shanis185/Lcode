class Solution(object):
    def numIslands(self, grid):
        r=len(grid)
        c=len(grid[0])

        def dfs(i,j):
            if i<0 or j< 0 or i>=r or j>=c or grid[i][j]!="1":
                return
            else:
                grid[i][j]="0"
                dfs(i,j+1)
                dfs(i+1,j)
                dfs(i,j-1)
                dfs(i-1,j)



        total=0
        for i in range(r):
            for j in range(c):
                if grid[i][j]=="1":
                    total+=1
                    dfs(i,j)
        return total
        