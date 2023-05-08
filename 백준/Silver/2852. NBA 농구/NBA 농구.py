import sys
input=sys.stdin.readline
n=int(input())
t1=t2=0
switch=0 #양수면 1번 팀이, 음수면 2번 팀이 이기는 중
for i in range(n):
    team,time=input().split()
    m,s=map(int,time.split(':'))
    if team=='1':
        if switch==0:
            t1+=48*60-(60*m+s) #초 단위로 바꾸고 전체(48분)시간에서 현재시간 빼기
        switch+=1 #1번 팀 득점
        if switch==0:
            if t2>0:
                t2-=(48*60-(60*m+s))
    else:
        if switch==0:
            t2+=48*60-(60*m+s)
        switch-=1
        if switch==0:
            if t1>0:
                t1-=(48*60-(60*m+s))
print(str(t1//60).zfill(2)+':'+str(t1%60).zfill(2))
print(str(t2//60).zfill(2)+':'+str(t2%60).zfill(2))