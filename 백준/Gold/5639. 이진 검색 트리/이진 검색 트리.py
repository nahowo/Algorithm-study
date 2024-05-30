import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**9)

def postorder(start,end):
    if start>end:
        return
    mid=end+1
    for i in range(start+1,end+1):
        if node[start]<node[i]:
            mid=i
            break
    postorder(start+1,mid-1)
    postorder(mid,end)
    print(node[start])

node=[]
while True:
    try:
        tmp=int(input())
        node.append(int(tmp))
    except:
        break
postorder(0,len(node)-1)