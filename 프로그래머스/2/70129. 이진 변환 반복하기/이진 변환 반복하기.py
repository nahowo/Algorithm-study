def removeZeros(s):
    return s.count('0')

def decimalToBinary(n):
    result = []
    while True:
        if n < 2:
            result.append(n)
            break
        result.append(n % 2)
        n //= 2
    
    for i in range(len(result) // 2 + 1):
        result[i], result[len(result) - i - 1] = str(result[len(result) - i - 1]), str(result[i])
    return ''.join(result)

def solution(s):
    answer = []
    changeCnt = 0
    removedZeroCnt = 0
    while True:
        if s == '1':
            break
        
        tmpCnt = removeZeros(s)
        removedZeroCnt += tmpCnt
        s = decimalToBinary(len(s) - tmpCnt)
        changeCnt += 1
    answer = [changeCnt, removedZeroCnt]
        
    return answer