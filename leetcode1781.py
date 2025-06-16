class Solution:
    def beautySum(self, s: str) -> int:
        count=0
        for i in range(len(s)):
            for j in range(i,len(s)):
                substr=s[i:j+1]
                counter=Counter(substr)
                count+=(max(counter.values())-min(counter.values()))
        return count