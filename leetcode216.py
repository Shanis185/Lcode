class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res=[]
        ans=[]

        def backtrack(x):
            if sum(ans)>n:
                return

            
            if len(ans)==k:    
                if sum(ans)==n:
                    res.append(ans[:])
                return
            
            
            for i in range(x,10):
                
                ans.append(i)
                backtrack(i+1)
                ans.pop()

        backtrack(1)
        return res
                