import sys
input=sys.stdin.readline
n,q=map(int,input().split())
land=[False]*(n+1)
answer=[]
for i in range(q):
    duck=int(input())
    first_occupied=-1
    tmp_duck=duck
    while tmp_duck!=0:
        if land[tmp_duck]==True:
            first_occupied=tmp_duck
        tmp_duck=tmp_duck//2
    if first_occupied==-1: #오리가 원하는 땅을 가진 경우
        land[duck]=True
        answer.append(0)
    else:
        answer.append(first_occupied)
for i in answer:
    print(i)