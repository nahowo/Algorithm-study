def solution(id_list, report, k):
    count={i:0 for i in id_list} # 신고자: 신고한 이용자 중 정지된 이용자 수
    record={i:set() for i in id_list} # 신고된 이용자: {신고한 이용자 1, 신고한 이용자 2, ...}
    for i in range(len(report)): # record 기록 작성
        reporter,reported=report[i].split()
        record[reported].add(reporter)
        
    for reported,reporters in record.items(): # 신고 횟수 확인
        if len(reporters)>=k:
            for j in list(reporters):
                count[j]+=1
    answer=list(count.values())
    
    return answer