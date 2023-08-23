import sys, math
input=sys.stdin.readline
n=int(input())
num=list(map(int,input().split()))
arr=[0]*63
for i in range(n):
    if num[i]!=0:
        tmp=int(math.log2(num[i]))
        arr[tmp]+=1
for i in range(62):
    arr[i+1]+=arr[i]//2
    if arr[i]!=0:
        M=2**(i)
if arr[62]!=0:
    M=2**(62)
print(M)