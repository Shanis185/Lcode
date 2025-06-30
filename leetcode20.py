class Solution:
    def isValid(self, s: str) -> bool:
        stk=[]
        
        for i in s:
            if i=="(" or i=="[" or i=="{":
                stk.append(i)
            else:
                if not stk:
                    return False
                if i=="]" and stk.pop()!="[":
                    
                    return False
                    
                if i=="}" and stk.pop()!="{":
                     
                    return False
                    
                if i==")" and stk.pop()!="(":
                
                    return False
        
        return len(stk)==0