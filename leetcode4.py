class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1)>len(nums2):
            nums1,nums2=nums2,nums1
        m,n=len(nums1),len(nums2)
        left=0
        right=m
        while left<=right:
            partitionx=(left+right)//2
            partitiony=(m+n+1)//2-partitionx
            maxleftx=nums1[partitionx-1] if partitionx>0 else float('-inf')
            minrightx=nums1[partitionx] if partitionx<m else float('inf')
            maxlefty=nums2[partitiony-1] if partitiony>0 else float('-inf')
            minrighty=nums2[partitiony] if partitiony<n else float('inf')

            if maxleftx<=minrighty and maxlefty<=minrightx:
                if (m+n)%2==0:
                    return (max(maxleftx,maxlefty)+min(minrightx,minrighty))/2.0
                else:
                    return float(max(maxleftx,maxlefty))
            elif maxleftx>minrighty:
                right=partitionx-1
            else:
                left=partitionx+1
        return 0
            