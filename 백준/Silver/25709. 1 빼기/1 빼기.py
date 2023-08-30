import sys
input=sys.stdin.readline
n=input().rstrip()
cnt=0
while True:
    if n=='0':
        break
    elif n=='1':
        cnt+=1
        break
    if '1' in n:
        n=str(int(n.replace('1','',1)))
        cnt+=1
    else:
        n=str(int(n)-1)
        cnt+=1
print(cnt)