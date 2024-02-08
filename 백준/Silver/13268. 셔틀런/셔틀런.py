n = int(input())
d = 0

while(n > 0):
    d = 0
    for i in 1,2,3,4:
        for j in range(i):
            n -= 5
            if n <= 0:
                d += 5+n
                break
            d += 5
        if n <= 0:
            break
            
        for j in range(i):
            n -= 5
            if n <= 0:
                d -= 5+n
                break
            d -= 5
        if n <= 0:
            break

print(d//5 if d%5 == 0 else d//5+1)