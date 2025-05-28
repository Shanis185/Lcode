class Solution(object):
    def maxAreaOfIsland(self, grid):
        
        r=len(grid)
        c=len(grid[0])
        maxi=0
        if not grid or not grid[0]:
            return 0

        def dfs(i,j):
            if i<0 or j<0 or i>=r or j>=c or grid[i][j]!=1:
                return 0
            grid[i][j]=-1
            area=1
            
            area+=dfs(i+1,j)
            
            area+=dfs(i,j+1)
                
            area+=dfs(i-1,j)
                
            area+=dfs(i,j-1)
                
            
            return area

        
        for i in range(r):
            for j in range(c):
                if grid[i][j]==1:
                    
                    
                    maxi=max(maxi,dfs(i,j))
        return maxi
        