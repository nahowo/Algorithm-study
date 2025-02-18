def solution(people, limit):
    answer = 0
    people.sort()
    start = 0
    end = len(people) - 1
    
    while start < end:
        if people[start] + people[end] > limit:
            end -= 1
        else:
            end -= 1
            start += 1
        answer += 1
    if start == end:
        answer += 1
    
    return answer