import sys
input=sys.stdin.readline
n=int(input())
map=input().rstrip()
tmp=0
for i in range(n-1):
    if map[i:i+2]=='EW':
        tmp+=1
print(tmp)