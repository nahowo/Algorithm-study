import sys
input=sys.stdin.readline
def compare():
    tmp=0
    for i in range(n):
        if status[i]!=target[i]:
            tmp+=1
    return tmp
t=int(input())
answer=[]
def func():
    tmp_ans=0
    sw=status.count('W')
    tw=target.count('W')
    mismatch=compare()
    tmp=mismatch-abs(sw-tw)
    if tmp==0:
        tmp_ans=mismatch
    else:
        tmp_ans=tmp//2+tmp%2+abs(sw-tw)
    return tmp_ans
for _ in range(t):
    n=int(input())
    status=input().rstrip()
    target=input().rstrip()
    answer.append(func())
for i in answer:
    print(i)