import sys
input=sys.stdin.readline

def func():
    n=int(input())
    arr=list(input().rstrip().split())
    submit=list(input().rstrip().split())
    d=dict() # 제출한 순서대로 인덱스값을 저장
    for i in range(n):
        d[submit[i]]=i

    point=0
    score=[1]*n
    for i in range(n-1,0,-1): # 제일 나중에 일어났던 해전부터 하나씩 탐색(i)
        key=d.get(arr[i],0) # 작성했던 답안에서 i 해전이 위치한 곳(몇 번째로 작성했는지)을 key로 잡기
        point+=sum(score[:key]) # i 해전보다 이전에 발생했다고 작성한 것의 합(옳은 답의 합)을 point에 누적
        score[key]=0 # i 해전 방문 처리(서로 다른 해전끼리만 순서를 비교)

    return str(point)+"/"+str(int(n*(n-1)*0.5))

print(func())