import sys
input=sys.stdin.readline
n=int(input())
beads=list(map(int,input().split()))
energy=0
def func(s):
    global energy
    if len(beads)==2:
        if s>energy:
            energy=s
        return
    else:
        for i in range(1,len(beads)-1):
            e=beads[i-1]*beads[i+1]
            tmp=beads[i]
            del beads[i]
            func(s+e)
            beads.insert(i,tmp)
func(0)
print(energy)