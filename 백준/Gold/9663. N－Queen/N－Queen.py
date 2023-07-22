import sys
input=sys.stdin.readline
n=int(input())
row=[0]*n
posible=0
def queen_check(x):
    for i in range(x):
        if row[x]==row[i] or abs(row[x]-row[i])==x-i:
            return False
    return True
def dfs(x):
    global posible
    if x==n:
        posible+=1
        return
    else:
        for i in range(n):
            row[x]=i
            if queen_check(x)==True:
                dfs(x+1)
dfs(0)
print(posible)