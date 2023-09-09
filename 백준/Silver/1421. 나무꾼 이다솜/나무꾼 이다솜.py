import sys
input=sys.stdin.readline
n,c,w=map(int,input().split())
tree=[int(input()) for _ in range(n)]
answer=0
for l in range(1,max(tree)+1):
    money=0
    for i in tree:
        if i%l==0:
            cost=(i//l)-1
        else:
            cost=i//l
        k=i//l
        cnt=(k*w*l)-cost*c
        if cnt>0:
            money+=cnt
    if money>answer:
        answer=money
print(answer)