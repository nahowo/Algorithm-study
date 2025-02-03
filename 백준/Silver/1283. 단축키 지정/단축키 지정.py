import sys
input = sys.stdin.readline

def shortCut(op):
    for i in range(len(op)):
        if i == 0 or op[i - 1] == " ":
            if op[i].upper() not in sc and op[i].lower() not in sc:
                return i
    
    for i in range(1, len(op)):
        if op[i - 1] == " ":
            continue
        if op[i] != " " and op[i].upper() not in sc and op[i].lower() not in sc:
            return i
    
    return -1

def solution():
    global sc
    n = int(input())
    sc = set()
    options = []
    for i in range(n):
        options.append(input().rstrip())
    
    for i in range(n):
        option = options[i]
        idx = shortCut(options[i])
        if idx > -1:
            sc.add(option[idx])
            newOption = option[:idx] + "[" + option[idx] + "]" + option[idx + 1:]
            options[i] = newOption
    for i in range(n):
        print(options[i])

solution()