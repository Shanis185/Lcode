class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if num==0:
            return 0
        if k==0:
            return num
        stk=[]
        for i in num:
            while stk and k>0 and int(stk[-1])>int(i):
                
                stk.pop()
                k-=1


            stk.append(i)
        stk=stk[:-k] if k>0 else stk


        res="".join(stk)
        
        res=res.lstrip('0')

        return res if res else "0"

        