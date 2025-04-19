import math

def lcm(a, b):
    return a * b // math.gcd(a, b)

def solution(arr):
    a = arr[0]
    for i in range(1, len(arr)):
        b = arr[i]
        a = lcm(a, b)
        
    return a