from collections import deque
class Solution(object):
    def pacificAtlantic(self, heights):
        p_queue=deque()
        p_seen=set()
        a_queue=deque()
        a_seen=set()
        m=len(heights)
        n=len(heights[0])


        for i in range(n):
            p_queue.append((0,i))
            p_seen.add((0,i))
        for j in range(1,m):
            p_queue.append((j,0))
            p_seen.add((j,0))
        for i in range(m):
            a_queue.append((i,n-1))
            a_seen.add((i,n-1))
        for j in range(n-1):
            a_queue.append((m-1,j))
            a_seen.add((m-1,j))
        
        def dfs(que,seen):
            while que:
                i,j=que.popleft()
                for i_,j_ in [(0,1),(1,0),(-1,0),(0,-1)]:
                    r,c=i+i_,j+j_
                    if 0<=r<m and 0<=c<n and heights[i][j]<=heights[r][c] and (r,c) not in seen:
                        que.append((r,c))
                        seen.add((r,c))
            return seen
        p_cord=dfs(p_queue,p_seen)
        a_cord=dfs(a_queue,a_seen)
        return list(p_cord.intersection(a_cord))