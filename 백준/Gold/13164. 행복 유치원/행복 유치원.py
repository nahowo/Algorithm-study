import sys
input=sys.stdin.readline
n,k=map(int,input().split())
student=list(map(int,input().split()))
height_difference=[]
for i in range(n-1):
    height_difference.append(student[i+1]-student[i])
height_difference.sort(reverse=True)
print(sum(height_difference[k-1:]))