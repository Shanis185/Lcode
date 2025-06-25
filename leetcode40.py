class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        ans=[]
        candidates.sort()
        def backtrack(x,total):
        
            if total==target:
                
                res.append(ans[:])
                return
            if total>target:
                return
            
            for i in range(x,len(candidates)):
                if i >x and candidates[i]==candidates[i-1]:
                    continue
                ans.append(candidates[i])
                backtrack(i+1,total+candidates[i])
                ans.pop()
        backtrack(0,0)
        return res