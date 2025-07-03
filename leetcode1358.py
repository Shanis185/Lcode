from collections import Counter
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count=0
        counter=Counter()
        l=0
        for i in range(len(s)):
            counter[s[i]]+=1
            while counter["a"]> 0 and counter["b"]>0 and counter["c"]>0:
                count+=len(s)-i
                counter[s[l]]-=1
                l+=1
        return count