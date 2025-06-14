class Solution:
    def largestOddNumber(self, num: str) -> str:
        res=[]
        final=[]
        n=len(num)
        for i in num:
            res.append(i)
        for i in range(len(res)):
            no=res.pop()
            if int(no)%2==1:
                res.append(no)
                return "".join(res)
        return ""
        

