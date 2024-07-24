def calcFee(fees, time):
    basicMin = fees[0]
    basicFee = fees[1]
    perMin = fees[2]
    perFee = fees[3]
    
    if time <= basicMin:
        return basicFee
    time -= basicMin
    tmp = time / perMin
    if int(tmp) != tmp:
        return basicFee + (int(tmp) + 1) * perFee
    else:
        return basicFee + int(tmp) * perFee

def calcTime(ent, ext):
    return ext - ent
    
def timeToMins(hour, minute):
    return 60 * hour + minute

def solution(fees, records):
    answer = []
    parked = dict()
    totalTime = dict()
    totalFee = dict()
    
    for i in range(len(records)):
        time, carNum, method = records[i].split()
        hour, minute = map(int, time.split(":"))
        mins = timeToMins(hour, minute)
        
        if method == 'IN':
            parked[carNum] = mins
        else: # method == 'OUT'
            prevMins = parked[carNum]
            totalMins = calcTime(prevMins, mins)
            totalTime[carNum] = totalTime.get(carNum, 0) + totalMins
            del parked[carNum]
    
    if parked: # 23:59까지 출차하지 않은 차량이 남아있는 경우
        for carNum, prevMins in parked.items():
            mins = timeToMins(23, 59)
            totalMins = calcTime(prevMins, mins)
            totalTime[carNum] = totalTime.get(carNum, 0) + totalMins
    
    for carNum, mins in totalTime.items():
        totalFee[carNum] = calcFee(fees, mins)
    
    parkingList = list(totalFee.items())
    parkingList.sort()
    for i in range(len(parkingList)):
        answer.append(parkingList[i][1])
    
    return answer