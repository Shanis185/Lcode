class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len=0
        string=""
        for i in range(len(s)):
            for j in range(i,len(s)):
                substr=s[i:j+1]
                if substr==substr[::-1] and len(substr)>max_len:
                    max_len=len(substr)
                    string=substr
        return string