import sys
input=sys.stdin.readline

n=int(input())
student=[]
for _ in range(n):
    student.append(input().rstrip())

length=len(student[0])
for i in range(length,-1,-1):
    s=set()
    for j in range(n):
        s.add(student[j][i:length+1])
    if len(s)==n:
        k=length-i
        break

print(k)