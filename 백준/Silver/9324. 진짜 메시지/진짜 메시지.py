import sys
input=sys.stdin.readline
t=int(input())
def SMTP(m):
    count=dict()
    check=False #변형으로 추가된 문자인지 확인
    for i in range(len(m)):
        if check==True:
            check=False
            continue
        count[str(m[i])]=count.get(str(m[i]),0)+1 #각 문자 수 딕셔너리에 저장
        if count[str(m[i])]==3: #문자 수가 3개째 나오면
            if (i!=len(m)-1 and m[i+1]!=m[i]) or (i==len(m)-1): #다음에 같은 문자가 있는지 / 마지막 문자인지 확인
                return 'FAKE'
            count[str(m[i])]=0 #아닐 경우 현재 문자 수는 0으로 되돌리기
            check=True
    return 'OK'
for _ in range(t):
    message=input().rstrip()
    print(SMTP(message))