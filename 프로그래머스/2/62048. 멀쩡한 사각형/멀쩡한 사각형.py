import math
def solution(w,h):
    gcd = math.gcd(w, h)
    sw, sh = w // gcd, h // gcd
        
    cnt = sw + sh - 1
    answer = w * h - (cnt * (w // sw))
    return answer