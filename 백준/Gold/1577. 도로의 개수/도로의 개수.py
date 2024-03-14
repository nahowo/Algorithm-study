import sys
input=sys.stdin.readline

def func():
    n,m=map(int,input().split())
    k=int(input())
    worked=set() # 공사중인 도로
    end=set() # 공사중인 도로의 끝
    for _ in range(k):
        a,b,c,d=map(int,input().rstrip().split())
        (t1,t2),(t3,t4)=sorted([(b,a),(d,c)]) # 공사중인 도로 정보를 시작-끝으로 정렬
        worked.add((t1,t2,t3,t4))
    
    city=[[0]*(n+1) for _ in range(m+1)]
    city[0][0]=1
    for i in range(m+1):
        for j in range(n+1):
            if i-1>=0:
                if (i-1,j,i,j) not in worked:
                    city[i][j]+=city[i-1][j]
            if j-1>=0:
                if (i,j-1,i,j) not in worked:
                    city[i][j]+=city[i][j-1]

    return city[m][n]

print(func())