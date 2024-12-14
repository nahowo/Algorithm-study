import sys
input = sys.stdin.readline

def splitList(arr, target):
    tmp = []
    for i in range(len(arr)):
        tmp.extend(list(arr[i].split(target)))
    return tmp

def solution():
    s = input().rstrip()
    splitted = [s]
    splitted = (splitList(splitted, 'pi'))
    splitted = (splitList(splitted, 'ka'))
    splitted = (splitList(splitted, 'chu'))
    
    for i in range(len(splitted)): 
        if splitted[i] != '':
            return "NO"
    return "YES"

print(solution())