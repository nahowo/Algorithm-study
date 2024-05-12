import sys
input=sys.stdin.readline

def func():
    minkyum=input().rstrip()
    maxV=''
    minV=''

    tmp=list(minkyum.split('K'))
    maxarr=[]
    tmparr=[]
    minarr=[]

    for i in range(len(tmp)):
        tmparr.append(tmp[i]+'K')
    if tmparr[-1][-1]=='K':
        tmparr[-1]=tmparr[-1][:-1]
    if tmparr[-1]=='':
        tmparr.pop()
    for i in range(len(tmparr)):
        t=tmparr[i]
        if len(t)==t.count('M'):
            for j in range(len(t)):
                maxarr.append(t[j])
        else:
            maxarr.append(tmparr[i])
    
    for i in range(len(tmp)):
        if tmp[i]!='':
            minarr.append(tmp[i])
        minarr.append('K')
    minarr.pop()

    maxV=''
    minV=''
    for i in maxarr:
        maxV+=check(i)
    for i in minarr:
        minV+=check(i)
    print(maxV)
    print(minV)
    return

def check(s):
    m=s.count('M')
    k=s.count('K')
    if k==0:
        answer=10**(m-1)
    else:
        answer=10**(m)*5
    return str(answer)

func()