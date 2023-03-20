import sys
input=sys.stdin.readline
a=input().rstrip()
b=input().rstrip()
name=''
apb=[3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
for i in range(len(a)):
    name+=a[i]
    name+=b[i]
arr=[]
for i in range(len(name)):
    arr.append(apb[ord(name[i])-65])
while len(arr)!=2:
    tmp=[]
    for i in range(len(arr)-1):
        tmp.append((arr[i]+arr[i+1])%10)
        #tmp.append(str(int(arr[i])+int(arr[i+1]))[-1:]) #int와 str에서 시간이 걸림
    arr=tmp
print(str(arr[0])+str(arr[1]))