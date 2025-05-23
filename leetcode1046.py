import heapq
class Solution(object):
    def lastStoneWeight(self, stones):
        
        for i in range(len(stones)):
            stones[i]=-stones[i]

        heapq.heapify(stones)
        
        while len(stones)>1:
            largest1=-heapq.heappop(stones)
            largest2=-heapq.heappop(stones)
            

            if largest1!=largest2:
                new=largest1-largest2
                heapq.heappush(stones,-new)
        if not stones:
            return 0
        return -stones[0]
