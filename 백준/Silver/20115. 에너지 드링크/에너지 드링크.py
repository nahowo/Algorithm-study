import sys
input=sys.stdin.readline
n=int(input())
drink=list(map(int,input().split()))
drink.sort()
answer=drink.pop()
answer+=sum(drink)/2
print(round(answer,5))