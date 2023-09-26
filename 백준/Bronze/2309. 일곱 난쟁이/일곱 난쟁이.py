import sys
input=sys.stdin.readline
sum=0
dwarf=[]
for i in range(9):
    dwarf.append(int(input()))
    sum+=dwarf[i]
d=sum-100
def found():
    for i in range(8):
        for j in range(i+1,9):
            if dwarf[i]+dwarf[j]==d:
                x,y=dwarf[i],dwarf[j]
                dwarf.remove(x)
                dwarf.remove(y)
                return
found()
dwarf.sort()
for i in dwarf:
    print(i)