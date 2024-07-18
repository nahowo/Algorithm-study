def solution(s):
    answer = []
    s = s[1:-1]
    
    tuples = []
    tmpArr = []
    tmp = ''
    for i in s:
        if i == "}":
            if tmp != '':
                tmpArr.append(int(tmp))
            tuples.append(tmpArr)
            tmpArr = []
            tmp = ''
        elif i.isnumeric():
            tmp += i
        elif i == ',':
            if tmp != '':
                tmpArr.append(int(tmp))
            tmp = ''
    tuples.sort(key = lambda x:len(x))
    
    element = set()
    for i in range(len(tuples)):
        tmpSet = set(tuples[i])
        tmpElement = list(tmpSet - element)[0] # 공집합 구하기
        answer.append(tmpElement)
        element.add(tmpElement)
    
    return answer