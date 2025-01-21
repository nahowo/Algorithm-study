import sys
input = sys.stdin.readline
flush = sys.stdout.flush
stdout = sys.stdout.write

def question(i):
    stdout('? ' + str(i) + '\n')
    flush()
    return int(input())

def solution():
    n = int(input())
    first = question(1)
    last = question(n)

    answer = last - first
    stdout('! ' + str(answer) + '\n')
    flush()
    return

solution()