import sys
input=sys.stdin.readline
    
def func():
    n,l=map(int,input().split())
    time=0
    place=0
    for _ in range(n):
        d,r,g=map(int,input().split())
        time+=d-place
        light=time%(r+g)
        if light<=r: # 빨간불인 경우
            time+=r-light # 남은 빨간불 시간동안 현재 위치에서 대기
        place=d
    time+=l-place
    return time

print(func())