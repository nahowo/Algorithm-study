def solution(queue1, queue2):
    l1, l2 = len(queue1), len(queue2)
    
    q1 = queue1 + [0] * l2 * 2
    q2 = queue2 + [0] * l1 * 2
    
    if (sum(queue1) + sum(queue2)) % 2 == 1:
        return -1
    goal = (sum(queue1) + sum(queue2)) // 2
    s1 = sum(queue1)
    cnt = 0
    p1, i1 = 0, l1
    p2, i2 = 0, l2
    
    while True:
        if i1 >= l1 + l2 + l2 or i2 >= l2 + l1 + l1:
            return -1
        if s1 < goal: # q2 -> q1
            q1[i1], q2[p2] = q2[p2], 0
            s1 += q1[i1]
            i1 += 1
            p2 += 1
        elif s1 > goal: # q1 -> q2
            q2[i2], q1[p1] = q1[p1], 0
            s1 -= q2[i2]
            p1 += 1
            i2 += 1
        else:
            return cnt
        cnt += 1
    
    return answer