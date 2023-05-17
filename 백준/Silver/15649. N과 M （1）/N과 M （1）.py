from itertools import permutations
n,m=map(int,input().split())
n=[i for i in range(1,n+1)]
perm=list(permutations(n,m))
for i in range(len(perm)):
    print(' '.join(map(str,perm[i])))