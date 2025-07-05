from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        char_count=defaultdict(int)
        for ch in t:
            char_count[ch]+=1
        
        start_index=0
        min_window=(0,float("inf"))
        remaining=len(t)
        for end,ch in enumerate(s):
            if char_count[ch]>0:
                remaining-=1
            char_count[ch]-=1

            if remaining==0:
                while True:
                    char_start=s[start_index]
                    if char_count[char_start]==0:
                        break
                    char_count[char_start]+=1
                    start_index+=1
                if end-start_index<min_window[1]-min_window[0]:
                    min_window=(start_index,end)

                char_count[s[start_index]]+=1
                remaining+=1
                start_index+=1

        return "" if min_window[1]==float("inf") else s[min_window[0]:min_window[1]+1]
                
        
            