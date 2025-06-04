import sys
from itertools import permutations
input = sys.stdin.readline
HEX = 0xF

def solution():
    global dictionary
    for L, I, S, T, F, O in permutations(range(0, 16), 6):
        # L, F, S는 0 불가능
        if L * F * S == 0:
            continue

        # 16 = 2^4, 각 알파벳에 4비트씩 할당
        LIST = (L << 12) + (I << 8) + (S << 4) + T
        FILO = (F << 12) + (I << 8) + (L << 4) + O
        STACK = LIST + FILO

        s = (STACK >> 16) & HEX
        t = (STACK >> 12) & HEX
        a = (STACK >> 8) & HEX
        c = (STACK >> 4) & HEX
        k = (STACK) & HEX
        # STACK 결과의 S, T가 할당한 S, T와 동일해야 함
        if s != S or t != T:
            continue

        # A, C, K는 L, I, S, T, F, O와 겹치면 안 됨
        dictionary = {L, I, S, T, F, O}
        result = isDuplicated([a, c, k])
        if result:
            print('{:04x} + {:04x} = {:05x}'.format(LIST, FILO, STACK))

def isDuplicated(chars):
    for v in chars:
        if v not in dictionary:
            dictionary.add(v)
        else:
            return False
    return True

solution()