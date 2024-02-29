import sys
input=sys.stdin.readline

def func():
    n=int(input())
    score=list(map(int,input().split()))+[0,0]
    dp=[0, score[0], score[0]+score[1]]

    for i in range(2, n+2):
        dp.append(max(dp[-1]+score[i], dp[-3]+(score[i-2]+score[i-1]+score[i])*2))

    return dp[-1]

print(func())