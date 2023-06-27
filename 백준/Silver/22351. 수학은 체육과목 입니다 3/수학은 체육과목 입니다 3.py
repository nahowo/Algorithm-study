import sys
input=sys.stdin.readline
s=input().rstrip()
arr=[s[:1],s[:2],s[:3]]
for a in arr:
    b=int(a)
    ns=''
    while len(ns)<len(s):
        ns+=str(b)
        b+=1
    if ns==s:
        print(int(a),b-1)
        break