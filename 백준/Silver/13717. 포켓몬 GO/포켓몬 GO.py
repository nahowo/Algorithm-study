import sys
input=sys.stdin.readline

def func():
    n=int(input())
    pokemon=[]
    maxpo=0
    maxdev=0
    dev=0

    for i in range(n):
        pokemon.append(input().rstrip())
        k,m=map(int,input().split())
        
        tmp=0
        while True:
            if m-k>=0:
                m-=k
                tmp+=1
                m+=2
            else:
                break

        if tmp>maxdev:
            maxdev=tmp
            maxpo=i
        dev+=tmp
    print(dev)
    print(pokemon[maxpo])

func()