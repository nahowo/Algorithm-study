import sys
input=sys.stdin.readline
m,n=map(int,input().split())
arr=['A','B','C','D','E','F']
data=''
if m==0:
    data='0'
while m>0:
    if m%n>=10:
        data+=str(arr[(m%n)-10])
    else:
        data+=str(m%n)
    m//=n
data=data[::-1]
print(data)