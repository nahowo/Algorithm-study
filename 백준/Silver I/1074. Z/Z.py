import sys
input=sys.stdin.readline

def func(x,y,n):
    global answer
    if x>r or x+n<=r or y>c or y+n<=c:
        answer+=n**2
        return
    if n>2:
        n//=2
        func(x,y,n)
        func(x,y+n,n)
        func(x+n,y,n)
        func(x+n,y+n,n)
    else:
        if x==r and y==c:
            print(answer) 
        elif x==r and y+1==c:
            print(answer+1)
        elif x+1==r and y==c:
            print(answer+2)
        else:
            print(answer+3)
        sys.exit()

n,r,c=map(int,input().split())
answer=0
func(0,0,2**n)