import sys
input=sys.stdin.readline

x=int(input())
n=int(input())
staff=dict()
chip=dict()
if n!=0:
    for _ in range(n):
        a,b=input().split()
        staff[a]=int(b)

    staff=dict(filter(lambda e:e[1]>=x*0.05, staff.items())) # 득표율이 5% 미만인 스태프 제거
    tmp=dict()
    for i in range(1,15):
        for k,v in staff.items():
            tmp[v/i]=k
    tmp=sorted(tmp.items(),reverse=True) # key 기준 내림차순 정렬
    for i in range(14): # 14번째까지 순위별 칩 지급
        best=tmp[i][1]
        chip[best]=chip.get(best,0)+1
    for i in staff: # 받은 칩이 0개인 스태프 추가
        if i[0] not in chip.keys():
            chip[i[0]]=0

    chip=dict(sorted(chip.items()))
    for k,v in chip.items():
        print(k,v)