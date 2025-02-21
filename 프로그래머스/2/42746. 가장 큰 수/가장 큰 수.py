def solution(numbers):
    n = len(numbers)
    nums = list(map(str, numbers))
    nums.sort(key = lambda x: x * 3, reverse = True)
    answer = ''.join(nums)
    if len(answer) == answer.count('0'):
        answer = '0'
    return answer