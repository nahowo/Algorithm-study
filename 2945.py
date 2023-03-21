import math
r,g=map(int,input().split())
gcd_=math.gcd(r,g)
tmp=int((gcd_)**(1/2))
num=[]
for i in range(1,tmp+1):
    if r%i==0 and g%i==0:
        num.append(i)
        if i**2!=gcd_:
            num.append(gcd_//i)
for i in num:
    print(i,r//i,g//i)