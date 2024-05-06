class Solution:
    def reverse(self, x: int) -> int:
        if x>=0:
            x=int(str(x)[::-1])
        else:
            x=(-1)*int(str((-1)*x)[::-1])
        
        k = 2**31
        if x<=-k or x>=k-1:
            x=0
        
        return x