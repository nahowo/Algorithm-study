def solution(nums):
    n = len(nums)
    cnt = n // 2
    d = dict()
    for i in range(n):
        d[nums[i]] = d.get(nums[i], 0) + 1
        
    return min(len(d), cnt)