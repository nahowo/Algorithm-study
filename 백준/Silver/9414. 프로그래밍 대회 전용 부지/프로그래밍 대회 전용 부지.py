import sys
input=sys.stdin.readline
t=int(input())
for _ in range(t):
    l=[]
    l_cnt=0
    while True:
        tmp=int(input())
        if tmp==0:
            break
        l.append(tmp)
        l_cnt+=1
    l.sort(reverse=True)
    cost=0
    for i in range(l_cnt):
        cost+=2*l[i]**(i+1)
    if cost>5*10**6:
        print("Too expensive")
    else:
        print(cost)