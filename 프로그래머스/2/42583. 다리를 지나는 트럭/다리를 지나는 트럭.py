from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0] * (bridge_length))
    bSum = 0
    time = 0
    
    for nxt in truck_weights:
        while bSum + nxt > weight:
            bSum -= bridge.pop()
            if bSum + nxt <= weight:
                bSum += nxt
                bridge.appendleft(nxt)
                time += 1
                break
            bridge.appendleft(0)
            time += 1
        else:
            bSum += nxt
            bridge.appendleft(nxt)
            bSum -= bridge.pop()
            time += 1
    time += bridge_length
        
    return time