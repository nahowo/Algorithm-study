import sys
input=sys.stdin.readline

def func():
    n=int(input())
    doll=list(map(int,input().split()))
    answer=0

    while len(doll)>0:
        tmp=set(doll)
        for i in tmp:
            del doll[doll.index(i)]
        answer+=1

    return answer
    
print(func())