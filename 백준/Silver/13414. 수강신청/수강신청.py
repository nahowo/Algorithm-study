import sys
input=sys.stdin.readline
k,l=map(int,input().split())
apply=[input().rstrip() for _ in range(l)]
new_apply=[]
double_check=set()
for student in apply[::-1]:
    if student not in double_check:
        double_check.add(student)
        new_apply.append(student)
new_apply=new_apply[::-1]
for i in range(min(k,len(new_apply))):
    print(new_apply[i])