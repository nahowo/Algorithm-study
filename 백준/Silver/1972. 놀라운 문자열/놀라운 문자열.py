import sys
input=sys.stdin.readline
def func(t):
    for i in range(1,len(t)): #i: 문자열의 i쌍
        d=[]
        for j in range(len(t)-i):
            tmp=t[j:i+j+1:i]
            if tmp in d:
                return t+' is NOT surprising.'
            d.append(tmp)
    return t+' is surprising.'
while True:
    word=input().rstrip()
    if word=='*':
        break
    print(func(word))