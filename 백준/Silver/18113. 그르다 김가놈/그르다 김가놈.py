import sys
input=sys.stdin.readline

def func():
    n,k,m=map(int,input().split())
    kimbap=[]
    for _ in range(n):
        tmp=int(input())
        if tmp<2*k and tmp-k>0: # 김밥 길이가 2k보다 작은 경우
            kimbap.append(tmp-k)
        elif tmp>2*k: # 김밥 길이가 2k보다 큰 경우(2k인 경우는 어차피 0이 되므로 제외)
            kimbap.append(tmp-2*k)

    if len(kimbap)==0:
        return -1
    
    start=1
    end=max(kimbap)
    p=-1
    while start<=end:
        mid=(start+end)//2
        tmpsum=0
        tmpsum=sum([i//mid for i in kimbap])
        if tmpsum<m:
            end=mid-1
        else:
            start=mid+1
            p=mid
    return p

print(func())