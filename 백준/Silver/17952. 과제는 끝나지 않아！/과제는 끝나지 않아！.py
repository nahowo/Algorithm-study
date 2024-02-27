import sys
input=sys.stdin.readline
    
def func():
    n=int(input())
    task=[]
    score=0
    for _ in range(n):
        tmp=input()
        try:
            if tmp[0]=='1':
                _,a,t=map(int,tmp.split())
                task.append([t-1,a])
            if task[-1][0]==0:
                score+=task[-1][1]
                task.pop()
            else:
                task[-1][0]-=1
        except IndexError:
            continue
    return score

print(func())