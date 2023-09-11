import sys
from collections import Counter
input=sys.stdin.readline
s,p=map(int,input().split())
dna=input().rstrip()
dna+='0'
c=list(map(int,input().split()))
word=['A','C','G','T']
password=0
d=Counter(dna[:p])
def check(cnt):
    for i in range(4):
        if cnt[word[i]]<c[i]:
            return 0
    return 1
for i in range(s-p+1):
    if check(d):
        password+=1
    start=dna[i]
    end=dna[i+p]
    d[start]=d.get(start,0)-1
    d[end]=d.get(end,0)+1
print(password)