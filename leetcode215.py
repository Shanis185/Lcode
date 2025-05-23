import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        
        n=len(nums)
        for i in range(n):
            nums[i]=-nums[i]
        heapq.heapify(nums)
        
        
        stk=[]
        for i in range(k):
            stk.append(heapq.heappop(nums))
            
        return -stk[k-1]