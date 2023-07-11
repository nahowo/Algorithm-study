import sys
input=sys.stdin.readline
n=int(input())
s=set()
gom_=0
for _ in range(n):
    tmp=input().rstrip()
    if tmp=="ENTER":
        s=set()
    else:
        if tmp not in s:
            s.add(tmp)
            gom_+=1
print(gom_)