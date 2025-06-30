class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        max_left=[0]*n
        max_right=[0]*n
        lwall=rwall=0
        for i in range(n):
            j=-i-1
            max_left[i]=lwall
            max_right[j]=rwall
            lwall=max(lwall,height[i])
            rwall=max(rwall,height[j])
        summ=0
        for i in range(n):
            pot=min(max_left[i],max_right[i])
            summ+=max(0,pot-height[i])
        
        return summ