class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len=0
        
        l=0
        sett=set()
        for r in range(len(s)):
            while s[r] in sett:
                sett.remove(s[l])
                l+=1

            w=(r-l)+1
            max_len=max(max_len,w)
            sett.add(s[r])
        return max_len