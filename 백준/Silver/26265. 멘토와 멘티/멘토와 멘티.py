import sys
input=sys.stdin.readline

def func():
    n=int(input())
    pair=dict()
    for _ in range(n):
        a,b=input().split()
        if a in pair:
            pair[a].append(b)
        else:
            pair[a]=[b]

    mento=list(pair.keys())
    mento.sort()
    for m in mento:
        tmp=list(pair[m])
        tmp.sort(reverse=True)
        for i in tmp:
            print(m,i)
    return
func()