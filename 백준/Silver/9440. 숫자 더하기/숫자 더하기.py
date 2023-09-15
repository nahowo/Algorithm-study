import sys
input=sys.stdin.readline
from collections import deque
while True:
    tmp=list(map(int,input().split()))
    n=tmp[0]
    if n==0:
        break
    arr=tmp[1:]
    arr.sort()
    num1=deque([])
    num2=deque([])
    number=[num1, num2]
    if n%2==1:
        if arr[0]==0:
            cnt=0
            for i in range(1,n):
                if arr[i]!=0:
                    if cnt==0:
                        tmp=arr[i]
                        del arr[i]
                        arr.insert(0,tmp)
                        cnt+=1
                    else:
                        tmp=arr[i]
                        del arr[i]
                        arr.insert(2,tmp)
                        break
        number[0].append(str(arr[0]))
        arr.remove(arr[0])
    else:
        if arr[0]==0:
            cnt=0
            for i in range(1,n):
                if arr[i]!=0:
                    if cnt==2:
                        break
                    if cnt<2:
                        tmp=arr[i]
                        del arr[i]
                        arr.insert(0,tmp)
                        cnt+=1
    for i in range(len(arr)):
        if len(number[i%2])!=0 and number[i%2][0]!=0:
            number[i%2].append(str(arr[i]))
        else:
            number[i%2].appendleft(str(arr[i]))
    print((int(''.join(number[0]))+int(''.join(number[1]))))