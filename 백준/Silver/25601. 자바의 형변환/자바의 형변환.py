import sys
input=sys.stdin.readline

def func():
    n=int(input())
    relation=dict()
    for _ in range(n-1):
        a,b=input().rstrip().split()
        relation[a]=b # relation = {자식: 부모}
    c1,c2=input().rstrip().split()

    # c1이 c2의 부모인지 확인(c1 고정)
    tmp=c2
    while True:
        if tmp==None: # tmp가 루트 노드
            break
        elif tmp==c1:
            return 1
        tmp=relation.get(tmp)
    
    # c2이 c1의 부모인지 확인(c2 고정)
    tmp=c1
    while True:
        if tmp==None: # tmp가 루트 노드
            break
        elif tmp==c2:
            return 1
        tmp=relation.get(tmp)
    return 0

print(func())