class Solution(object):
    def networkDelayTime(self, times, n, k):
        graph=defaultdict(list)
        for u,v,time in times:
            graph[u].append((v,time))
        min_time={}
        min_heap=[(0,k)]
        while min_heap:
            delay,i=heapq.heappop(min_heap)
            if i in min_time:
                continue
            min_time[i]=delay
            for neigh,neightime in graph[i]:
                if neigh not in min_time:
                    heapq.heappush(min_heap,(delay+neightime,neigh))
        if len(min_time)==n:
            return max(min_time.values())
        else:
            return -1