import sys
from fractions import Fraction
input=sys.stdin.readline
n,m=map(int,input().split())
sugar=[]
for _ in range(n):
    w,v=map(int,input().split())
    sugar.append([w,v])
sugar.sort(key=lambda x:-(x[1]/x[0]))
sugar_level=Fraction(0)
for w,v in sugar:
    if m==0:
        break
    a=min(m,w)*v
    b=w
    sugar_level+=Fraction(a,b)
    m-=min(m,w)
print(str(sugar_level.numerator)+'/'+str(sugar_level.denominator))