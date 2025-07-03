class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
       max_len=0
       l=0
       n=len(nums)
       for r in range(n):
            if nums[r]==0:
                k-=1
            while k<0:
                if nums[l]==0:
                    k+=1
                l+=1


            w=(r-l)+1
            max_len=max(max_len,w)
       return max_len
            


        