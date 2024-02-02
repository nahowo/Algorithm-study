import sys
from itertools import combinations
input=sys.stdin.readline

def compare(a,b):
    cnt=0
    for i in range(len(a)):
        if a[i]!=b[i]:
            cnt+=1
    return cnt

t=int(input())
def func():
    n=int(input())
    mbti=list(input().rstrip().split())
    distance=sys.maxsize
    
    if len(mbti)>32:
        return 0
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                tmp=0
                if i!=j and j!=k and i!=k:
                    tmp+=compare(mbti[i],mbti[j])
                    tmp+=compare(mbti[i],mbti[k])
                    tmp+=compare(mbti[j],mbti[k])
                    distance=min(tmp,distance)
    return distance

for _ in range(t):
    print(func())