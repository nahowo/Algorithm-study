import sys
input=sys.stdin.readline

def clockNum(n):
    numlist=[]
    for i in range(4):
        tmp=''
        for j in range(4):
            tmp+=n[(i+j)%4]
        numlist.append(int(tmp))
    Min=min(numlist)
    return Min

def func():
    num=list(input().split())
    tmpMin=clockNum(num) # 현재 시계수

    cnt=1
    for a in range(1,10):
        for b in range(1,10):
            for c in range(1,10):
                for d in range(1,10):
                    tmp=a*1000+b*100+c*10+d
                    if tmp==tmpMin:
                        return cnt
                    else:
                        if tmp==clockNum(list(str(tmp))):
                            cnt+=1
    
print(func())