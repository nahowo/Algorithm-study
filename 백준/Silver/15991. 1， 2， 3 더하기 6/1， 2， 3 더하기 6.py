import sys
input=sys.stdin.readline
t=int(input())
num=[int(input()) for _ in range(t)]
m=max(num)
arr=[1,1,2,2,3,3]
for i in range(6,m+1):
    arr.append((arr[i-2]+arr[i-4]+arr[i-6])%1000000009)
for i in num:
    print(arr[i])