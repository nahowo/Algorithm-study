class Solution:
    def climbStairs(self, n: int) -> int:
        a,b=1,2
        if n==1:
            return a
        for i in range(2,n):
            a,b=b,a+b
        return b