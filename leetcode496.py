class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        stk=[]
        next_great={}
        res=[]
        for i in nums2:
            while stk and i>stk[-1]:
                smaller=stk.pop()
                next_great[smaller]=i

            stk.append(i)

        for i in stk:
            next_great[i]=-1
        
        for i in nums1:
            res.append(next_great[i])
        return res
                
