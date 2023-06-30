import sys
input=sys.stdin.readline
s=input().rstrip()
q=int(input())
tmpd=dict()
cnt=[tmpd]
answer=[]
for i in range(len(s)):
    tmpd2=tmpd.copy()
    tmp=s[i]
    tmpd2[tmp]=tmpd2.get(tmp,0)+1
    cnt.append(tmpd2)
    tmpd=tmpd2.copy()
for i in range(q):
    a,l,r=input().split()
    answer.append(cnt[int(r)+1].get(a,0)-cnt[int(l)].get(a,0))
print(*answer)