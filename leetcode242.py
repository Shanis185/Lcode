from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1=Counter(s)
        dict2=Counter(t)
        return dict1==dict2