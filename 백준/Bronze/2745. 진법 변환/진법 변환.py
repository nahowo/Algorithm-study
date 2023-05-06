import sys
input=sys.stdin.readline
a=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
n,b=input().split()
n=n[::-1]
result=0
for i in range(len(n)):
    if n[i].isdigit():
        result+=((int(b))**i)*int(n[i])
    else:
        result+=((int(b))**i)*(a.index(n[i])+10)
print(result)