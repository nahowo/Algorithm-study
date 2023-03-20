import sys
input=sys.stdin.readline
n,k=map(int,input().split())
temp=list(map(int,input().split())) #온도 배열
pre_sum=[0]
tmp=0
for i in range(n): #누적합 배열 생성
    tmp+=temp[i]
    pre_sum.append(tmp)
k_temp=[] #연속적인 k일의 온도의 합 배열
for i in range(1,n-k+2): #유효 누적합은 인덱스 1부터 시작
    a,b=i,i+k-1
    k_temp.append(pre_sum[i+k-1]-pre_sum[i-1])
print(max(k_temp)) #연속적인 k일의 온도의 합의 최대