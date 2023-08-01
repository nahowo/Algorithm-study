import sys
input=sys.stdin.readline
t=int(input())
for _ in range(t):
    recorded=input().rstrip().split()
    fox_sound=[]
    animal_sound=set()
    while True:
        sound=input().rstrip()
        if sound=="what does the fox say?":
            break
        animal_sound.add(sound.split()[2])
    for i in recorded:
        if i not in animal_sound:
            fox_sound.append(i)
    print(*fox_sound)