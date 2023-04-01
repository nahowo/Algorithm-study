import sys
input=sys.stdin.readline
n=int(input())
num=list(map(int,input().split()))
consi=[num[0]]
for i in range(n-1):
    consi.append(max(consi[i]+num[i+1],num[i+1]))
print(max(consi))