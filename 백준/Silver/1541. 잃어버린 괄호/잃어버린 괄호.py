import sys
input=sys.stdin.readline

def func():
    formula=input().rstrip().split('-')
    arr=[]
    for i in formula:
        tmp=i.split('+')
        tmpsum=0
        for j in tmp:
            tmpsum+=int(j)
        arr.append(tmpsum)
    return arr[0]-sum(arr[1:])
print(func())