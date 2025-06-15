class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.lstrip()
        if not s :
            return 0
        sign=1
        i=0
        
        if i<len(s) and s[i]=='+':
            i+=1
        elif i<len(s) and s[i]=="-":
            i+=1
            sign=-1
        total=0
        while i<len(s):
            curr=s[i]
            if not curr.isdigit():
                break
            
            total=(total*10)+int(curr)
            i+=1
        total*=sign

        if total<-2**31:
            return -2**31
        elif total>2**31-1:
            return 2**31-1
        
        else:
            return total


