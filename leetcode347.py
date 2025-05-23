import heapq
from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
           stk=[]
           counter=Counter(nums)
           for key,value in counter.items():
                heapq.heappush(stk,(value,key))
                if len(stk)>k:
                    heapq.heappop(stk)
           return [key for value,key in stk]
           