
class Solution(object):
    def minEatingSpeed(self, piles, h):
        
        def k_works(k):
            hours=0
            for p in piles:
                hours+=(p+k-1)//k
            return hours<=h

        left=1
        right=max(piles)
        while left<right:
            mid=(left+right)//2
            if k_works(mid):
                right=mid
            else:
                left=mid+1
        return left



      