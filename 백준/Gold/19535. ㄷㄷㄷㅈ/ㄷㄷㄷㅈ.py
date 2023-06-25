import sys
import math
input=sys.stdin.readline
n=int(input())
edge=[]
d=[0]*(n+1)
for _ in range(n-1):
    a,b=map(int,input().split())
    edge.append([a,b])
    d[a]+=1
    d[b]+=1
def d_tree():
    answer=0
    for a,b in edge:
        cnt=(d[a]-1)*(d[b]-1)
        answer+=cnt
    return answer
def g_tree():
    answer=0
    for s in range(1,n+1):
        if d[s]>=3:
            answer+=math.comb(d[s],3)
    return answer
D=d_tree()
G=g_tree()
if D>G*3:
    print('D')
elif D<G*3:
    print('G')
else:
    print('DUDUDUNGA')