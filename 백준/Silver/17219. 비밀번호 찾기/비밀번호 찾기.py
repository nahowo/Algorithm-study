import sys
import heapq
input=sys.stdin.readline

def func():
    n,m=map(int,input().split())
    password=dict()
    for _ in range(n):
        site,p=input().rstrip().split()
        password[site]=p
    
    for _ in range(m):
        site=input().rstrip()
        print(password.get(site))

func()