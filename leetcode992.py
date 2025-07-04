from collections import defaultdict
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atmost(k):
            l=0
            counter=defaultdict(int)
            res=0
            for r in range(len(nums)):
                if counter[nums[r]]==0:
                    k-=1
                counter[nums[r]]+=1

                while k<0:
                    counter[nums[l]]-=1
                    if counter[nums[l]]==0:
                        k+=1
                    l+=1

                res+=r-l+1
            return res

        return atmost(k)-atmost(k-1)