def spliting(fileName):
    head = ''
    number = 0
    headFlag = False
    numberFlag = False
    
    for i in fileName:
        if not i.isnumeric() and not headFlag:
            head += i
        elif i.isnumeric() and not numberFlag:
            headFlag = True
            tmpNumber = number * 10
            tmpNumber += int(i)
            if 0 <= tmpNumber <= 99999:
                number = tmpNumber
            else:
                numberFlag = True
        else:
            numberFlag = True
    
    head = head.lower()
    return head, number

def solution(files):
    answer = []
    original = dict()
    
    arr = []
    for i in range(len(files)):
        original[i] = files[i]
        head, number = spliting(files[i])
        arr.append([head, number, i])
    
    arr.sort()
    for i in arr:
        answer.append(original[i[2]])
    
    return answer