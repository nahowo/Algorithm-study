import sys
input=sys.stdin.readline
    
def func():
    n=int(input())
    m=int(input())
    if m==10:
        return abs(n-100)
    elif m==0:
        return min(abs(n-100),len(str(n)))
    broken=set(input().rstrip().split())


    answer=sys.maxsize

    for i in range(1000001):
        tmp=str(i)
        for j in range(len(tmp)):
            if tmp[j] in broken:
                break
            elif j==len(tmp)-1:
                answer=min(answer,abs(int(tmp)-n)+len(tmp))

    answer=min(answer,abs(n-100))
    return answer

print(func())