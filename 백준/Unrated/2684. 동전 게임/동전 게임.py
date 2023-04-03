import sys
input=sys.stdin.readline
t=int(input())
seq=['TTT','TTH','THT','THH','HTT','HTH','HHT','HHH']
for _ in range(t):
    ans=[0]*8
    case=input()
    for i in range(38):
        ans[seq.index(case[i:i+3])]+=1
    print(*ans)