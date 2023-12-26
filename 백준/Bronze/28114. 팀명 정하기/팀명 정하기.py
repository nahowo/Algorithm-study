import sys
input=sys.stdin.readline

team=[]
for _ in range(3):
    team.append(list(input().rstrip().split()))

key=[]
for i in range(3):
    key.append(int(team[i][1])%100)
key.sort()
name1=''.join(list(map(str,key)))

key=[]
for i in range(3):
    key.append([team[i][2][0],int(team[i][0])])
key.sort(key=lambda x:-x[1])
for i in range(3):
    key[i]=key[i][0]
name2=''.join(key)

print(name1)
print(name2)