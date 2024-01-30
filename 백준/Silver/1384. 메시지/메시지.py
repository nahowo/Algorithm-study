import sys
input=sys.stdin.readline

g=1
while True:
    n=int(input())
    if n==0:
        break
    kids=[]
    bad_words=[]
    flag=False
    for i in range(n):
        tmp=list(input().rstrip().split())
        kids.append(tmp[0])
        if tmp[1:].count("N")>0:
            flag=True
            for j in range(1,n):
                if tmp[j]=="N":
                    bad_words.append([(i-j)%n,i])

    print("Group "+str(g))
    if not flag:
        print("Nobody was nasty")
    else:
        for i in bad_words:
            print(kids[i[0]]+" was nasty about "+kids[i[1]])
    print("")
    g+=1