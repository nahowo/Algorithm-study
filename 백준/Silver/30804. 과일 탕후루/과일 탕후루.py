'''
DP 테이블 초기화
배열 순회
    과일 빈도수 딕셔너리, 현재까지의 과일 종류 개수 업데이트
	종류 개수>2:
        while 종류 개수>2:
            맨 뒤 과일 제거
			딕셔너리 업데이트
	DP[i]=현재 탕후루 길이
max(DP) 출력
'''

import sys
input=sys.stdin.readline

def main():
    n=int(input())
    fruit=list(map(int,input().split()))
    dp=[0]*n
    dp[0]=1
    fruitDict=dict()
    fruitDict[fruit[0]]=1
    fruitCnt=1
    start=0

    for i in range(1,len(fruit)):
        if fruit[i] not in fruitDict:
            fruitDict[fruit[i]]=1
            fruitCnt+=1
        else:
            fruitDict[fruit[i]]+=1
        
        while fruitCnt>2:
            removed=fruit[start]
            fruitDict[removed]-=1
            if fruitDict[removed]==0:
                del fruitDict[removed]
                fruitCnt-=1
            start+=1
        
        dp[i]=i-start+1
    
    return max(dp)

print(main())

# 시간복잡도: for문 안에 while문이 있지만 슬라이딩 윈도우 형식이므로 O(n)