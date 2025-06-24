class Solution:
    def myPow(self, x: float, n: int) -> float:
        def pow(x,n):
            return float(x**n)

        return pow(x,n)