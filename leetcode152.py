class Solution(object):
    def maxProduct(self, nums):
        product=1
        max_prod=float('-inf')
        for num in nums:
            product*=num
            max_prod=max(max_prod,product)
            if num==0:
                product=1
        
        product=1
        for num in reversed(nums):
            product*=num
            max_prod=max(max_prod,product)
            if num==0:
                product=1
        return max_prod