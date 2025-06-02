class Solution(object):
    def majorityElement(self, nums):
       hashmap={}
       for i in nums:
            if i in hashmap:
                hashmap[i]+=1
            else:
                hashmap[i]=1
       max_key=max(hashmap,key=hashmap.get)
       return max_key