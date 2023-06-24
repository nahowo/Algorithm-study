import sys
input=sys.stdin.readline
t=int(input())
def func():
    n=int(input())
    number=[]
    for _ in range(n):
        number.append(input().rstrip())
    number.sort()
    for i in range(n-1):
        tlen=len(number[i])
        if number[i]==number[i+1][:tlen]:
            print('NO')
            return
    print('YES')
for _ in range(t):
    func()