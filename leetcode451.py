class Solution:
    def frequencySort(self, s: str) -> str:
        dict1=defaultdict(int)
        for i in s:
            dict1[i]+=1
        sorted_=sorted(dict1.items(),key=lambda x:x[1],reverse=True)
        res=[]
        for i,j in sorted_:
            while j>0:
                res.append(i)
                j-=1
        return "".join(res)

             