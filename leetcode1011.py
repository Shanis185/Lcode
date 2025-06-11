class Solution(object):
    def shipWithinDays(self, weights, days):
        left=max(weights)
        right=sum(weights)
        def capacity(mid):
            t_days=1
            total=0
            for i in weights:
                if total+i>mid:
                    t_days+=1
                    total=0
                total+=i
            return t_days<=days


        while left<right:
            mid=(left+right)//2
            if capacity(mid):
                right=mid
            else:
                left=mid+1
        return left

        