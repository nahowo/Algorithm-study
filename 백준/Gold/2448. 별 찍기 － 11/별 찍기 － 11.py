import sys
input=sys.stdin.readline
from math import log2

def func():
    n=int(input())
    k=int(log2(n//3))
    triangle=["*","* *","*****"] # 기본 삼각형
    for i in range(k):
        tmp=triangle.copy() # 첫번째 삼각형 채우기
        blank=(3*2**(i+1))-1 # 공백 개수
        for j in range(len(tmp)): # 중간 공백 채우기
            tmp[j]+=(' '*blank)
            blank-=2
        for j in range(len(tmp)): # 두번째 삼각형 채우기
            tmp[j]+=triangle[j]
        triangle.extend(tmp) # 새 삼각형으로 업데이트
    
    for i in range(n): # 앞, 뒤 공백 채우기
        triangle[i]=(' '*(n-i-1))+triangle[i]+(' '*(n-i-1))
    
    for i in triangle:
        print(i)

func()