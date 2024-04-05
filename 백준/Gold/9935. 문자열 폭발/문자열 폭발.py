import sys
input=sys.stdin.readline

def func():
    s=list(input().rstrip())
    bomb=list(input().rstrip())

    stack=[]
    stackL=0
    bombL=len(bomb)

    for i in s:
        if stackL<bombL:
            stack.append(i)
            stackL+=1
        else:
            if stack[(stackL-bombL):]==bomb:
                for j in range(bombL):
                    stack.pop()
                stackL-=bombL
            stack.append(i)
            stackL+=1

    if stack[(stackL-bombL):]==bomb:
        for j in range(bombL):
            stack.pop()
        stackL-=bombL
    if stackL==0:
        stack='FRULA'
    return ''.join(stack)

print(func())