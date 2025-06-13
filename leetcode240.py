class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        j=n-1
        for i in range(m):
            while j>=0 and matrix[i][j]>target:
                j-=1
            if matrix[i][j]==target:
                return True
        return False