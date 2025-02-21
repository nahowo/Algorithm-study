import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    nums = list(map(str, input().split()))
    nums.sort(key = lambda x: x * 10, reverse = True)
    answer = ''.join(nums)
    if len(answer) == answer.count('0'):
        answer = '0'
    return answer

print(solution())