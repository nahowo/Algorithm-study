import sys
input=sys.stdin.readline
apb=[3,2,1,2,4,3,1,3,1,1,3,1,3,2,1,2,2,2,1,2,1,1,1,2,2,1]
n,m=map(int,input().split())
a,b=input().split()
name=''
for i in range(min(n,m)): #두개의 이름 번갈아가며 합치기
    name+=a[0]
    name+=b[0]
    a=a[1:]
    b=b[1:]
name+=a+b
arr=[]
for i in name:
    arr.append(apb[ord(i)-ord('A')])
while len(arr)!=2:
    tmp=[]
    for i in range(len(arr)-1):
        tmp.append((arr[i]+arr[i+1])%10)
    arr=tmp
print(str(arr[0]*10+arr[1])+'%')