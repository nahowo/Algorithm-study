import sys
input=sys.stdin.readline

t=int(input())

def func():
    n=int(input())
    clothes=dict()
    res=1

    for _ in range(n):
        _,category=input().rstrip().split()
        clothes[category]=clothes.get(category,1)+1
    
    for i in clothes.values(): # 분류별 옷의 개수 + 안 입는 경우(1)
        res*=i
    return res-1 # 아무 옷도 입지 않는 경우 제외

for _ in range(t):
    print(func())