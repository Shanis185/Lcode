class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m=len(mat)
        n=len(mat[0])
        left=0
        right=n-1
        while left<=right:
            mid=(left+right)//2
            max_index=0
            for i in range(m):
                if mat[i][mid]>mat[max_index][mid]:
                    max_index=i
            left_val=mat[max_index][mid-1] if mid-1>=0 else -1
            right_val=mat[max_index][mid+1] if mid+1<=n-1 else -1
            curr_val=mat[max_index][mid]

            if curr_val>=left_val and curr_val>=right_val:
                return [max_index,mid]
            elif curr_val<right_val:
                left=mid+1
            else:
                right=mid-1
        return [-1,-1]