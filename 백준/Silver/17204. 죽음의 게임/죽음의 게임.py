import sys
input=sys.stdin.readline

def func():
    n,k=map(int,input().split())
    graph=[]

    for _ in range(n):
        graph.append(int(input()))
    
    cnt=1
    i=0
    for _ in range(n):
        tmp=graph[i] # tmp는 i가 지목한 사람
        if tmp!=k and tmp!=0 and tmp!=i: # 지목된 사람이 영기나 보성이가 아니고, 자신을 지목하지 않은 경우
            cnt+=1
        elif tmp==k: # 보성이를 찾은 경우
            break
        elif i!=0 and tmp==0: # 영기인 경우
            break
        elif i==0 and tmp==0: # 영기가 자신을 지목한 경우
            break
        i=tmp

    if tmp!=k:
        return -1
    else:
        return cnt

print(func())