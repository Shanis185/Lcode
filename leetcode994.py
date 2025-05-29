class Solution(object):
    def orangesRotting(self, grid):
        m=len(grid)
        n=len(grid[0])
        fresh,rotten,empty=1,2,0
        num_fresh=0
        q=deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j]==fresh:
                    num_fresh+=1
                elif grid[i][j]==rotten:
                    q.append((i,j))
        if num_fresh==0:
            return 0
        minutes=-1
        while q:
            q_size=len(q)
            minutes+=1
            for i in range(q_size):
                i,j=q.popleft()
                for i_,j_ in[(0,1),(1,0),(-1,0),(0,-1)]:
                    r,c=i+i_,j+j_
                    if 0<=r<m and 0<=c<n and grid[r][c]==fresh:
                        grid[r][c]=rotten
                        num_fresh-=1
                        q.append((r,c))
        if num_fresh==0:
            return minutes
        return -1

        
        