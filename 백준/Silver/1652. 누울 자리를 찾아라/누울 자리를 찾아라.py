import sys
input=sys.stdin.readline

def check(arr):
    cnt=0
    for i in range(len(arr[0])):
        tmp=arr[i].split('X')
        for j in tmp:
            if '..' in j:
                cnt+=1
    return cnt

def func():
    n=int(input())
    room_vertical=[]
    room_horizontal=['' for _ in range(n)]
    for i in range(n):
        tmp=input().rstrip()
        room_vertical.append(tmp)
        for j in range(n):
            room_horizontal[j]+=tmp[j]
    
    vertical=check(room_vertical)
    horizontal=check(room_horizontal)


    print(vertical, horizontal)

func()