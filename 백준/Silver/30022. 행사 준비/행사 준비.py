import sys
input=sys.stdin.readline

# 1. n개의 p,q에서 p-q를 기준으로 내림차순 정렬
# 2. 앞에서 A개는 동하가, 뒤에서 B개는 지원이가 구매

# n개의 물건 정보를 입력받아 계산하는 함수
def main():
    n,a,b=map(int,input().split())
    price=[]
    for _ in range(n):
        p,q=map(int,input().split())
        price.append([p,q,p-q])
    price.sort(key=lambda x:x[2]) # 정렬에 O(nlogn)

    answer=0
    for i in range(a):
        answer+=price[i][0]
    for i in range(n-1,n-b-1,-1):
        answer+=price[i][1]
    
    return answer

print(main())

# 전체 시간복잡도: O(nlogn)