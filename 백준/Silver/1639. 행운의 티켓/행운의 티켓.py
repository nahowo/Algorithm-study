import sys
input=sys.stdin.readline

def func():
    s=list(map(int,list(input().rstrip())))
    n=len(s)
    arr=[0]
    answer=0

    for i in range(n): # 누적합 계산
        arr.append(arr[i]+s[i])
    
    for i in range(1,n//2+1):
        for j in range(i*2,n+1):
            try:
                left=arr[j-i]-arr[j-i*2]
                right=arr[j]-arr[j-i]
                if left==right:
                    answer=max(answer,i*2)
            except:
                continue
    return answer

print(func())