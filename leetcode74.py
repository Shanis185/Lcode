class Solution(object):
    def searchMatrix(self, matrix, target):
        m=len(matrix)
        n=len(matrix[0])
        left=0
        right=(m*n)-1
        while left<=right:
            mid=(left+right)//2
            row=mid//n
            col=mid%n
            midval=matrix[row][col]
            if midval==target:
                return True
            elif midval<target:
                left=mid+1
            else:
                right=mid-1
        return False