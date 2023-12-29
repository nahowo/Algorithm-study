import sys
import heapq
input=sys.stdin.readline

t=int(input())
def func():
    k=int(input())
    minq=[]
    maxq=[]
    res="EMPTY"
    check=[0]*k

    for i in range(k):
        command,integer=input().rstrip().split()
        if command=='I':
            heapq.heappush(minq,(int(integer),i))
            heapq.heappush(maxq,(int(integer)*(-1),i))
            check[i]=True
        else:
            if integer=='1':
                while len(maxq)>0 and not check[maxq[0][1]]:
                    heapq.heappop(maxq)
                if len(maxq)>0:
                    check[maxq[0][1]]=False
                    heapq.heappop(maxq)
            else:
                while len(minq)>0 and not check[minq[0][1]]:
                    heapq.heappop(minq)
                if len(minq)>0:
                    check[minq[0][1]]=False
                    heapq.heappop(minq)

    while len(minq)>0 and not check[minq[0][1]]:
        heapq.heappop(minq)
    while len(maxq)>0 and not check[maxq[0][1]]:
        heapq.heappop(maxq)
    if len(minq)>0:
        res=str((-1)*maxq[0][0])+" "+str(minq[0][0])
    return res
for _ in range(t):
    print(func())