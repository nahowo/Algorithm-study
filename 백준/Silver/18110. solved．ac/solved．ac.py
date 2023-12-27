import sys
input=sys.stdin.readline

n=int(input())
difficulty=0
if n>0:
    rate=[]
    for _ in range(n):
        rate.append(int(input()))
    rate.sort()
    cut=int((n*15/100)+0.5)
    if cut>0:
        rate=rate[cut:-cut]
    difficulty=int(sum(rate)/(n-(cut*2))+0.5)
print(difficulty)