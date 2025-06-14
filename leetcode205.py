
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        dictt=defaultdict(list)
        for i in range(len(s)):
            dictt[s[i]].append(t[i])
        seen=[]
        for i,j in dictt.items():
            if len(set(j))!=1 or set(j) in seen:
                return False
            seen.append(set(j))
            
        return True
