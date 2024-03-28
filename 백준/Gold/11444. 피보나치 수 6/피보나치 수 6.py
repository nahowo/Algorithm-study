import sys
input=sys.stdin.readline

n=int(input())
basicM=[[1,1],[1,0]]

def func(a,b):
    if b==1:
        return a
    
    tmp=func(a,b//2)
    if b%2==0:
        return matrix_mul(tmp,tmp)
    else:
        return matrix_mul(matrix_mul(tmp,tmp),a)

def matrix_mul(m1,m2):
    answer=[[0,0],[0,0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                answer[i][j]+=m1[i][k]*m2[k][j]%1000000007
    return answer

matrix=func(basicM,n)
print(matrix[0][1]%1000000007)