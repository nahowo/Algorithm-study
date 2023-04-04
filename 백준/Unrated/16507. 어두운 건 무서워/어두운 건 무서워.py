import sys
input=sys.stdin.readline
R,C,Q=map(int,input().split())
photo=[]
for _ in range(R):
    tmp=list(map(int,input().split()))
    tmp3=0
    tmp2=[0]
    for i in tmp:
        tmp3+=i
        tmp2.append(tmp3)
    photo.append(tmp2) #누적합 리스트 생성
for _ in range(Q):
    sum_=0
    r1,c1,r2,c2=map(int,input().split())
    for i in range(r1-1,r2):
        sum_+=photo[i][c2]-photo[i][c1-1]
    div=(r2-r1+1)*(c2-c1+1)
    print(sum_//div)