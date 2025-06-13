class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return -1
        m=len(mat)
        n=len(mat[0])
        max_index=0
        count=0
        j=n-1
        for row in mat:
            row.sort()
        for i in range(m):
            
            while j>=0 and mat[i][j]==1:
                j-=1
                max_index=i
                count+=1
        return [max_index,count]