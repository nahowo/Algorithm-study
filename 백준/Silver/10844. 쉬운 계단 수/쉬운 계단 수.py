import sys
input=sys.stdin.readline
n=int(input())
possible=[0,1,1,1,1,1,1,1,1,1] # 현재 인덱스에서 이동 가능한 위치 개수
possible_tmp=[0]*10
for i in range(n-1):
    for j in range(10):
        if j==0:
            possible_tmp[1]+=possible[0]
        elif j==9:
            possible_tmp[8]+=possible[9]
        else:
            possible_tmp[j-1]+=possible[j]
            possible_tmp[j+1]+=possible[j]
    possible=possible_tmp.copy()
    possible_tmp=[0]*10
print(sum(possible)%1000000000)