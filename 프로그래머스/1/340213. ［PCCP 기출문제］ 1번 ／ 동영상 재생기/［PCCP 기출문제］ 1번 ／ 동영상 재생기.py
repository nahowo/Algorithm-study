def solution(video_len, pos, op_start, op_end, commands):
    def toT(t):
        mm, ss = t.split(':')
        return int(mm) * 60 + int(ss)
    
    def toMMSS(t):
        mm, ss = t // 60, t % 60
        return mm, ss

    def isOpBetween(t):
        if ost <= t <= oet:
            return oet
        return t

    et = toT(video_len)
    t = toT(pos)
    ost = toT(op_start)
    oet = toT(op_end)

    for cmd in commands:
        t = isOpBetween(t)
        if cmd == "next":
            t = min(t + 10, et)
        elif cmd == "prev":
            t = max(t - 10, 0)
        t = isOpBetween(t)
    
    mm, ss = toMMSS(t)
    answer = '{0:02d}:{1:02d}'.format(mm, ss)

    return answer