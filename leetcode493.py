class Solution(object):
    def reversePairs(self, nums):
        def merge(start,end):
            if end-start<=1:
                return 0
            mid=(start+end)//2
            count=merge(start,mid)+merge(mid,end)
            j=mid
            for i in range(start,mid):
                while j<end and nums[i]>2*nums[j]:
                    j+=1
                count+=j-mid
            temp=[]
            i,j=start,mid
            while i<mid and j<end:
                if nums[i]<nums[j]:
                    temp.append(nums[i])
                    i+=1
                else:
                    temp.append(nums[j])
                    j+=1
            while i<mid:
                temp.append(nums[i])
                i+=1
            while j<end:
                temp.append(nums[j])
                j+=1
            nums[start:end]=temp
            return count







        return merge(0,len(nums))