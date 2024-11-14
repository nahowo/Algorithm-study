def decimalToTernaryReversed(n):
    result = 0
    while True:
        if n < 3:
            result *= 10
            result += n
            break
        result *= 10
        result += n % 3
        n //= 3
        
    return result
    
def ternaryToDecimal(n):
    result = 0
    l = len(str(n))
    for i in range(l):
        result += (n % 10) * (3 ** i)
        n //= 10
    
    return result

def solution(n):
    answer = ternaryToDecimal(decimalToTernaryReversed(n))
    return answer