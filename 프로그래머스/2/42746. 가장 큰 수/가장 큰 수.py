def solution(numbers):
    maxint = str(max(numbers))
    numbers = list(map(str,numbers))
    numbers.sort(key = lambda x : x * len(maxint))
    numbers=numbers[:: -1]
    answer=str(int(''.join(numbers)))
    return answer
