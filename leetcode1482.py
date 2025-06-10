class Solution(object):
    def minDays(self, bloomDay, m, k):
        if m*k>len(bloomDay):
            return -1
        def helper(mid):
            boquette=0
            flowers=0
            for i in bloomDay:
                if i<=mid:
                    flowers+=1
                    if flowers==k:
                        boquette+=1
                        flowers=0
                else:
                    flowers=0
            return boquette>=m




        left=min(bloomDay)
        right=max(bloomDay)
        while left<right:
            mid=(left+right)//2
            if helper(mid):
                right=mid
            else:
                left=mid+1
        return left

        