class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        for i in range(len(strs[0])):
            char=strs[0][i]
            for j in strs[1:]:
                if i>=len(j) or j[i]!=char:
                    return strs[0][:i]
        return strs[0]
    
    ***********************************************************
    class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        strs.sort()
        first=strs[0]
        last=strs[-1]
        i=0
        while i<len(first) and first[i]==last[i]:
            i+=1
        return first[:i] 
    

