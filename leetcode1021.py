class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        balance=0
        res=[]
        for i in s:
            if i=='(':
                if balance>0:
                    res.append(i)
                balance+=1
            else:
                balance-=1
                if balance>0:
                    res.append(i)
        return "".join(res)