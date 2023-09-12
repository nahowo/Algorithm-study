import sys
input=sys.stdin.readline
n=int(input())
w1=[500]
w2=[1000,1500]
answer=[]
for _ in range(n):
    car=0
    m=int(input())
    left=set(map(int,input().split()))
    right=set(map(int,input().split()))
    for t in left:
        if t+500 in left and t+1000 in right and t+1500 in right:
            car+=1
    answer.append(car)
for i in answer:
    print(i)