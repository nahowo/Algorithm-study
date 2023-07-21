import sys
input=sys.stdin.readline
triangle=set()
tmp=1
for i in range(2,10**5):
    triangle.add(tmp)
    tmp+=i
    n=0
while True:
    n+=1
    a,b=map(int,input().split())
    if a==0 and b==0:
        break
    cnt=0
    for i in range(int(a**(1/2)+1), int(b**(1/2))+1):
        if (i**2)-1 in triangle and i**2>a and i**2<b:
            cnt+=1
    print('Case '+str(n)+': '+str(cnt))