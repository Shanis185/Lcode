class Solution(object):
    def rotate(self, nums, k):
        
        d2=deque(nums)
        k%=len(d2)
        for i in range(k):
            d2.appendleft(d2.pop())
        for i in range(len(d2)):
            nums[i]=d2[i]

        