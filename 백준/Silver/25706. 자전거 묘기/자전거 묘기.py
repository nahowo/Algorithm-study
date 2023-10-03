import sys
input=sys.stdin.readline
n=int(input())
jump=list(map(int,input().split()))
cnt=[0]*n
cnt[n-1]=1
for i in range(n-2,-1,-1):
    if jump[i]==0:
        cnt[i]=cnt[i+1]+1
    else:
        if jump[i]+i+1>=n:
            cnt[i]=1
        else:
            cnt[i]=cnt[jump[i]+i+1]+1
print(*cnt)