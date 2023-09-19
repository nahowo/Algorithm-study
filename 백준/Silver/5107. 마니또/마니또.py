import sys
input=sys.stdin.readline
cnt=1
while True:
    n=int(input())
    if n==0:
        break
    s=[]
    for i in range(n):
        f,t=map(str,input().split())
        flag=False
        for j in s:
            if f in j or t in j:
                j.add(f)
                j.add(t)
                flag=True
                break
        if flag==False:
            s.append(set([f,t]))
    print(cnt,len(s))
    cnt+=1