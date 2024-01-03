import sys
input=sys.stdin.readline

total_room=0
room=[0]*12
n,p=map(int,input().split())
for i in range(n):
    s,y=map(int,input().split())
    room[s*6+(y-1)]+=1

for i in range(12):
    if room[i]%p==0:
        total_room+=room[i]//p
    else:
        total_room+=(room[i]//p)+1

print(total_room)