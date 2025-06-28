class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res=[]
        def backtrack(index,path,value,prev):
            if index==len(num):
                if value==target:
                    res.append(path)
                    return
            
            for i in range(index,len(num)):
                if i!=index and num[index]=="0":
                    break
                curr_str=num[index:i+1]
                curr_num=int(curr_str)

                if index==0:
                    backtrack(i+1,curr_str,curr_num,curr_num)
                
                else:
                    backtrack(i+1,path+"+"+curr_str,value+curr_num,curr_num)

                    backtrack(i+1,path+"-"+curr_str,value-curr_num,-curr_num)

                    backtrack(i+1,path+"*"+curr_str,value-prev+prev*curr_num,prev*curr_num)


        backtrack(0,"",0,0)
        return res