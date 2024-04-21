class Solution:
    def getSum(self, a: int, b: int) -> int:
        cnt=[None]*2000
        if a>=0:
            for _ in range(a):
                cnt.append(None)
        else:
            for _ in range(0,a,-1):
                cnt.pop()
        if b>=0:
            for _ in range(b):
                cnt.append(None)
        else:
            for i in range(0,b,-1):
                cnt.pop()
        return len(cnt)-2000