import sys
input=sys.stdin.readline

# 1. 선호도 조합에서 '- - -' 질의를 학생 수로 초기화
# 2. 학생 선호도를 입력받아 해당 질의의 value값 +1
# 3. 학생 선호도와 '-'를 조합해 가능한 질의의 value값 +1
# 4. 질의를 입력받아 해당하는 

# '-'가 적용된 필터 정보에 학생 수를 더하는 함수
def makeUnfilteredQuery(query):
    arr=list(query.split())
    filtered=['-','-','-']
    # '-'가 1개인 경우
    for i in range(3):
        tmp=filtered.copy()
        tmp[i]=arr[i]
        preference[' '.join(tmp)]=preference.get(' '.join(tmp),0)+1
    
    # '-'가 2개인 경우
    for i in range(3):
        tmp=arr.copy()
        tmp[i]='-'
        preference[' '.join(tmp)]=preference.get(' '.join(tmp),0)+1

# 선호도와 질의를 입력받아 처리하는 함수
def main():
    for _ in range(n): # 선호도 조합을 작성하는 과정에서 O(n*3)
        query=input().rstrip()
        preference[query]=preference.get(query,0)+1
        makeUnfilteredQuery(query)
    
    for _ in range(m): # 질의 확인 과정에서 O(m)
        query=input().rstrip()
        if query in preference:
            print(preference[query])
        else:
            print(0)

n,m=map(int,input().split())
# 선호도 조합별 학생 수 딕셔너리
preference={'- - -':n}

main()

# 전체 시간복잡도: O(n*3)