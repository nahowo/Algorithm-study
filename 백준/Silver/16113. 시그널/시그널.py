import sys
input=sys.stdin.readline

def func():
    global signal,number, n
    n=int(input())
    tmp=input().rstrip()
    signal=[]
    answer=''
    for i in range(5):
        s=i*(n//5)
        e=(i+1)*(n//5)
        signal.append(tmp[s:e])
    
    number = [
        ['###','#.#','#.#','#.#','###'],
        ['#','#','#','#','#'],
        ['###','..#','###','#..','###'],
        ['###','..#','###','..#','###'],
        ['#.#','#.#','###','..#','..#'],
        ['###','#..','###','..#','###'],
        ['###','#..','###','#.#','###'],
        ['###','..#','..#','..#','..#'],
        ['###','#.#','###','#.#','###'],
        ['###','#.#','###','..#','###'],
    ]

    for i in range(n//5): # 맨 윗줄
        for j in range(10): # number 번호
            if check(i,j)!=False:
                answer+=str(j)

    return answer

def check(i,j):
    for k in range(5):
        if signal[k][i:i+len(number[j][k])]!=number[j][k]:
            return False
        if j==1:
            if n//5==1:
                continue
            if i==0:
                if signal[k][i+1]!='.':
                    return False
            elif i==n//5-1:
                if signal[k][i-1]!='.':
                    return False
            else:
                if signal[k][i+1]!='.' or signal[k][i-1]!='.':
                    return False
    return True

print(func())