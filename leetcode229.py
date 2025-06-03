class Solution(object):
    def majorityElement(self, nums):
        n=len(nums)
        r=n//3
        res=[]
        count=Counter(nums)
        for i,j in count.items():
            if j>r:
                res.append(i)
        return res
        