'''
팀 구성 완료 테이블(check) 초기화
학생별 순회
    본인을 고른 경우 팀 구성 완료(아래에서 방문처리 하기 이전에 수행해야 함)

    if 방문하지 않은 경우:
        방문 처리
        스택에 추가
        팀 배열에 추가
        
        while 스택:
            방문하지 않은 팀원을 계속 추가
        
        팀원 배열에서 사이클을 찾아 사이클 길이만큼 팀 구성 완료
전체 학생 수 - 팀 구성 완료 학생에 추가
'''

import sys
input=sys.stdin.readline

def main():
    n=int(input())
    pick=[0]+list(map(int,input().split()))
    check=[False]*(n+1)
    teamed=0

    for x in range(1,n+1):
        if x==pick[x]: # 본인을 고른 경우
            teamed+=1
            check[x]=True

    for x in range(1,n+1):

        if not check[x]:
            check[x]=True
            stack=[x]
            teammate=[x]

            while stack:
                i=stack.pop()
                ni=pick[i]

                if not check[ni]:
                    check[ni]=True
                    teammate.append(ni)
                    stack.append(ni)
            
            for j in range(len(teammate)):
                if teammate[j]==ni:
                    teamed+=len(teammate)-j
                    break
    
    return n-teamed

t=int(input())
for _ in range(t):
    print(main())

# 시간복잡도: 방문 처리에서 O(n), 배열 구성 완료에서도 O(n)이 걸리지만 점점 줄어듦