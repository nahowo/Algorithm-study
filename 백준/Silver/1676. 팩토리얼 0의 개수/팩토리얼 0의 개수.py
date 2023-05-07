import sys
input=sys.stdin.readline
n=int(input())
f=1
for i in range(2,n+1):
    f*=i
f=str(f)[::-1]
answer=0
for i in range(len(f)):
    if f[i]!='0':
        break
    answer+=1
print(answer)