
class Solution(object):
    def kClosest(self, points, k):
        def f(x,y):
            return x**2+y**2
        heap=[]
        for i,j in points:
            d=f(i,j)
            if len(heap)<k:
                heapq.heappush(heap,(-d,i,j))
            else:
                heapq.heappushpop(heap,(-d,i,j))
        return [(i,j) for d,i,j in heap]