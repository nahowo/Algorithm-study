import sys
input=sys.stdin.readline
t=int(input())
num=[[] for _ in range(10)]
d=[1,-1,3,-3]
for i in range(1,10):
    for di in d:
        if di+i>=1 and di+i<=9:
            if (i%3==0 and di==1) or (i%3==1 and di==-1):
                continue
            else:
                num[i].append(di+i)
num[0].append(7)
num[7].append(0)
for _ in range(t):
    n=int(input())
    possible_tmp=[1]*(10)
    possible=[1]*(10)
    for i in range(1,n):
        for j in range(10):
            possible[j]=sum(possible_tmp[k] for k in num[j])
        possible_tmp=possible.copy()
    print(sum(possible)%1234567)