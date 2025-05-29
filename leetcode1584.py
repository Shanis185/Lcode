class Solution(object):
    def minCostConnectPoints(self, points):
        seen=set()
        min_cost=0
        min_heap=[(0,0)]
        n=len(points)
        while len(seen)<n:
            dist,i=heapq.heappop(min_heap)
            if i in seen:
                continue
            seen.add(i)
            min_cost+=dist
            xi,yi=points[i]
            for j in range(n):
                if j not in seen:
                    xj,yj=points[j]
                    dist=abs(xi-xj)+abs(yi-yj)
                    heapq.heappush(min_heap,(dist,j))
        return min_cost


        