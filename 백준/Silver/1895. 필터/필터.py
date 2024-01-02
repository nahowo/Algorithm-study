import sys
input=sys.stdin.readline

r,c=map(int,input().split())
image=[]
new_image=[]
for i in range(r):
    image.append(list(map(int,input().split())))
t=int(input())
pixel=0

for i in range(r-2):
    for j in range(c-2):
        tmplist=[]
        for k in range(i,i+3):
            for l in range(j,j+3):
                tmplist.append(image[k][l])
        tmplist.sort()
        if tmplist[4]>=t:
            pixel+=1
        new_image.append(tmplist[4]) # 중앙값

print(pixel)