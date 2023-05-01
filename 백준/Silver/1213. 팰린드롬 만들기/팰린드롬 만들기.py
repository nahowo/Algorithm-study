import sys
input=sys.stdin.readline
def func():
    if len(name)%2==0:
        for i in d.values():
            if i%2!=0:
                return 0
        return 1
    else:
        switch=0
        for i,j in d.items():
            if switch==1 and j%2!=0:
                return 0
            if j%2!=0:
                switch=1
                key=i
        return key
name=input().rstrip()
d=dict()
for i in name:
    d[i]=d.get(i,0)+1
ans=func()
if ans==0:
    print("I'm Sorry Hansoo")
else:
    d=sorted(d.items())
    p=[]
    for i in range(len(d)):
        for _ in range(d[i][1]//2):
            p.append(d[i][0])
    p=''.join(p)
    if ans==1:
        p+=p[::-1]
    else:
        p=p+ans+p[::-1]
    print(p)