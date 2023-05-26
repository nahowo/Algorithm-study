import sys
input=sys.stdin.readline
n,m=map(int,input().split())
arr=list(map(int,input().split()))
left,right=0,1
answer=0
while right<=n and left<=right:
    sum_=sum(arr[left:right])
    if sum_==m:
        answer+=1
        right+=1
    elif sum_<m:
        right+=1
    else:
        left+=1
print(answer)