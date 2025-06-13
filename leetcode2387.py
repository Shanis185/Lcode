import bisect
class Solution:
    def findMedian(self, matrix):
        m=len(matrix)
        n=len(matrix[0])
        left=min(row[0] for row in matrix)
        right=max(row[-1] for row in matrix)
        while left<=right:
            mid=(left+right)//2
            count=0
            for row in matrix:
                count+=bisect.bisect_left(row,mid)
            if count==(m*n)//2:
                return mid
            elif count<(m*n)//2:
                left=mid+1
            else:
                right=mid-1