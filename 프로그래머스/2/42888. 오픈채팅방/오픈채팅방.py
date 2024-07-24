def solution(record):
    answer = []
    nameDict = dict()
    messageDict = {"Enter": "님이 들어왔습니다.", "Leave": "님이 나갔습니다."}
    message = []
    
    for r in record:
        tmp = r.split()
        uId = tmp[1]
        if tmp[0] == "Enter":
            userName = tmp[2]
            nameDict[uId] = userName
            message.append([tmp[0], uId])
        elif tmp[0] == "Change":
            userName = tmp[2]
            nameDict[uId] = userName
        else: # tmp[0] == "Leave"
            message.append([tmp[0], uId])
    
    for i in range(len(message)):
        printMessage = message[i][0]
        userName = message[i][1]
        answer.append(nameDict[userName] + messageDict[printMessage])
        
    return answer