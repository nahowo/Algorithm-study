def solution(numbers):
    maxLen = len(str(max(numbers)))
    nums = list(map(str, numbers))
    nums.sort(key = lambda x: (x * maxLen), reverse = True)
    answer = ''.join(nums)
    if answer.count('0') == len(answer):
        answer = '0'
    return answer