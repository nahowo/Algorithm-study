import sys
input=sys.stdin.readline
t=int(input())
words=[]
for i in range(t):
    tmp=input().rstrip()
    words.append(tmp.split())
for i in range(t):
    for j in range(len(words[i])):
        print(words[i][j][::-1],end=' ')
    print()