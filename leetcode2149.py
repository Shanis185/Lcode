class Solution(object):
    def rearrangeArray(self, nums):
        neg,pos=[],[]
        n=len(nums)
        res=[]
        for i in nums:
            if i<0:
                neg.append(i)
            else:
                pos.append(i)
        m=n/2
        neg.reverse()
        pos.reverse()
        for i in range(m):
            res.append(pos.pop())
            res.append(neg.pop())
        return res
        