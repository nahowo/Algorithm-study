import sys
input=sys.stdin.readline
n,m=map(int,input().split())
dna=[input() for _ in range(n)]
answer=''
hd=0
for i in range(m):
    d=dict()
    for j in range(n):
        d[dna[j][i]]=d.get(dna[j][i],0)+1
    d=sorted(d.items(),key=lambda x:(-x[1],x[0]))
    answer+=d[0][0]
    for j in range(n):
        if dna[j][i]!=answer[i]:
            hd+=1
print(answer)
print(hd)