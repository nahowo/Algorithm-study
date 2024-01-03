import sys
input=sys.stdin.readline

n=int(input())
boj=[]
other=[]

for _ in range(n):
    tmp=input().rstrip()
    if tmp[:7]=='boj.kr/':
        try:
            number=int(tmp[7:])
            if 1<=number<=30000:
                boj.append(number)
            else:
                other.append(tmp)
        except:
            other.append(tmp)
    else:
        other.append(tmp)

other.sort(key=lambda x:(len(x),x))
boj.sort()

for i in other:
    print(i)
for i in boj:
    print("boj.kr/"+str(i))