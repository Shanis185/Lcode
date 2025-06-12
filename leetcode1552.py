class Solution(object):
    def maxDistance(self, position, m):
        def helper(mid):
            count=1
            last_ball=position[0]
            for i in range(1,len(position)):
                if position[i]-last_ball>=mid:
                    count+=1
                    last_ball=position[i]
                    if count==m:
                        return True
            return False


        position.sort()
        left,right=1,position[-1]-position[0]
        best_dist=0
        while left<=right:
            mid=(left+right)//2
            if helper(mid):
                left=mid+1
                best_dist=mid
            else:
                right=mid-1
        return best_dist
        
        