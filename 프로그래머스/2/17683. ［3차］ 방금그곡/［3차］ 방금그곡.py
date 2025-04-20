def getTime(start, end):
    start = start.split(":")
    end = end.split(":")
    return (int(end[0]) - int(start[0])) * 60 + int(end[1]) - int(start[1])

def checkMusic(sheet, m, times):
    totalMusic = sheet * times
    return m in totalMusic

def sharp2lower(sheet):
    ret = ""
    for i in range(len(sheet) - 1):
        if sheet[i] == '#':
            continue
        if sheet[i + 1] == '#':
            ret += sheet[i].lower()
        else:
            ret += sheet[i]
    if sheet[len(sheet) - 1] != '#':
        ret += sheet[len(sheet) - 1]
    return ret

def solution(m, musicinfos):
    m = sharp2lower(m)
    answer = "(None)"
    longest = 0

    for i, v in enumerate(musicinfos):
        start, end, name, sheet = v.split(",")
        sheet = sharp2lower(sheet)
        duration = getTime(start, end)
        length = len(sheet)

        played = sheet * (duration // length) + sheet[:(duration % length)]
        print(played)
        if m in played and duration > longest:
            answer = name
            longest = duration
    
    return answer