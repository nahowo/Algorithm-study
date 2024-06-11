import sys
input=sys.stdin.readline

# 배열을 입력받는 함수
def inputArr():
    n=int(input())
    # 1. 원소값 입력받기
    arr=[]
    for _ in range(n):
        arr.append(int(input()))
    global arrSet
    arrSet=set(arr.copy()) # 존재 여부 확인을 위한 집합

    # 2. 원소별로 올바른 배열 만들기
    answer=4 # 추가해야 할 원소의 최소 개수
    for i in arr:
        answer=min(answer,makeRightArr(i))
    
    return answer

# 입력받은 정수를 이용해 올바른 배열을 만드는 함수
def makeRightArr(a):
    minCnt=4 # 추가해야 할 원소의 최소 개수; 4개의 원소 추가 시 무조건 올바른 배열을 만들 수 있으므로 4로 초기화
    for i in range(a-4,a+1): # 올바른 배열의 시작 원소
        cnt=0
        for j in range(i,i+5):
            if j not in arrSet:
                cnt+=1
        minCnt=min(minCnt,cnt)
    return minCnt

print(inputArr())
# 원소값이 1,2,3,4인 경우: makeRightArr에서 음수도 고려하게 되지만 존재하지 않는 것은 동일