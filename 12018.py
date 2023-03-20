import sys
input=sys.stdin.readline
n,m=map(int,input().split())
arr=[]
def func():
    for _ in range(n):
        p,l=map(int,input().split())
        M=sorted(list(map(int,input().split())),reverse=True) #신청한 마일리지 내림차순 정렬
        if p<l:
            arr.append(1)
        else:
            arr.append(M[l-1])
func()
arr.sort()
lecture=0
for i in arr:
    if m-i<0:
        break
    m-=i
    lecture+=1
print(lecture)