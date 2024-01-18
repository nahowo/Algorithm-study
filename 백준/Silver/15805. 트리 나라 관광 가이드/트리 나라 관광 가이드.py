import sys
input=sys.stdin.readline

def func():
    n=int(input())
    route=list(map(int,input().split()))
    stack=[]
    parent=dict()

    for i in route:
        if len(stack)==0:
            parent[i]=-1 # 스택이 비어있다면 해당 도시의 부모는 없음(-1)
            stack.append(i)
            continue
        elif len(stack)>0 and i not in parent.keys(): # 스택이 비어있지 않고 해당 도시가 처음 등장한 경우
            parent[i]=stack[-1]

        if parent.get(stack[-1])==i: # 현재 도시가 이전 도시의 부모인지 확인
            stack.pop()
        else:
            stack.append(i)
    parent=dict(sorted(parent.items()))
    return parent

d=func()
print(len(d))
print(*d.values())