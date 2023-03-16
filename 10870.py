import sys
sys.setrecursionlimit(10**6)
n=int(input())
def fibo(a,b,count):
    if count==n:
        print(a)
        return 0
    fibo(b,a+b,count+1)
fibo(0,1,0)