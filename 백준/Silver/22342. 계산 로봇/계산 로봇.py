import sys
input=sys.stdin.readline

def func():
    m,n=map(int,input().split())

    # 가중치
    d=[]
    for _ in range(m):
        d.append(list(map(int,list(input().rstrip()))))

    # 저장값
    save=[[0]*n for _ in range(m)]
    
    # 출력값
    output=[[0]*n for _ in range(m)]
    for i in range(m):
        output[i][0]=d[i][0]
    
    # 출력값들 중 최대를 저장값에 저장(저장값 최대 업데이트), 저장값+가중치를 출력값에 저장
    for j in range(1,n): # 열
        for i in range(m): # 행
            tmp=[]
            for k in range(i-1,i+2):
                if 0<=k<m:
                    tmp.append(output[k][j-1])
            save[i][j]=max(tmp) # 저장값 계산
            output[i][j]=save[i][j]+d[i][j]
    
    maxSave=0
    for i in save: # 최대값 계산
        maxSave=max(max(i),maxSave)

    return maxSave

print(func())