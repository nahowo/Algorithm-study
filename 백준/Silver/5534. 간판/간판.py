import sys
input=sys.stdin.readline

def func():
    n=int(input())
    name=input().rstrip()
    arr=[]
    for _ in range(n):
        arr.append(input().rstrip())
    cnt=0
    
    for i in range(n): # 간판 번호
        cnt+=check(arr[i],name)
    return cnt

def check(s,name):
    for sidx in range(len(s)): # 시작 인덱스
        if s[sidx]==name[0]:
            for dist in range(1,len(s)//(len(name)-1)+1): # 간격 거리
                k=0
                for j in range(sidx,len(s),dist):
                    try:
                        if name[k]==s[j]:
                            k+=1
                            if k==len(name):
                                return True
                        else:
                            break
                    except IndexError:
                        break
    return False

print(func())