import sys
input=sys.stdin.readline
k,l,n=map(int,input().split())
data=input().rstrip()
stand=False
c0=0 #count 0
c1=0 #count 1
flag=False
for i in range(n):
    if data[i]=='1':
        c1+=1
        c0=0
    elif data[i]=='0':
        c1=0
        c0+=1
    if c1==k:
        stand=True
        c1=0
    if stand==True:
        if c0==l:
            print(i+1)
            flag=True
            stand=False
            c0=0
if stand==True:
    print(i+1+l-c0)
elif stand==False and flag==False:
    print('NIKAD')