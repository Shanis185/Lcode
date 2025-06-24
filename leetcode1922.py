class Solution:
    def countGoodNumbers(self, n: int) -> int:
        odd=n//2
        even=(n+1)//2
        mod=10**9+7
        def power(x,y):
            x=x%mod
            result=1

            while y>0:
                if y%2==1:
                    result=(result*x)%mod
                x=(x*x)%mod
                y=y//2
            return result
        total=(power(5,even)*power(4,odd))%mod
        return total