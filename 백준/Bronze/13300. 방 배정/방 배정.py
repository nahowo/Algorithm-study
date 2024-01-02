import sys
input=sys.stdin.readline

total_room=0
room=[0]*12
n,p=map(int,input().split())
for i in range(n):
    s,y=map(int,input().split())
    room[s*6+(y-1)]+=1

for i in range(12):
    if 0<room[i]<p:
        total_room+=1
    else:
        total_room+=int((room[i]/p)+0.5)

print(total_room)