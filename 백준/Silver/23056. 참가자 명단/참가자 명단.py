import sys
input=sys.stdin.readline

def func():
    n,m=map(int,input().split())
    classes={i:[] for i in range(1,n+1)}
    while True:
        a,b=input().split()
        if a=='0' and b=='0':
            break
        classes[int(a)].append(b)
    for i in classes.keys():
        tmp=classes[i]
        tmp=tmp[:m]
        tmp.sort(key=lambda x:(len(x),x))
        classes[i]=tmp
    
    for i in range(1,n+1,2): # 홀수(청팀)
        if len(classes[i])>0:
            for j in range(min(m,len(classes[i]))):
                print(i,classes[i][j])
    
    for i in range(2,n+1,2): # 짝수(백팀)
        if len(classes[i])>0:
            for j in range(min(m,len(classes[i]))):
                print(i,classes[i][j])

func()