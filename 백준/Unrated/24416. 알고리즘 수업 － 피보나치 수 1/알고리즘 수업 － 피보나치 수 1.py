n=int(input())
f=[0]*50
f[1]=f[2]=1
count=0
def fibo_dp(n):
    global count
    for i in range(3,n+1):
        f[i]=f[i-1]+f[i-2]
        count+=1
    return f[n]
print(fibo_dp(n),count)