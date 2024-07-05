/*
user - {유저: 유저번호}
reportTable - 신고한 유저 * 신고된 유저 형식의 2차원 배열
reportUser - {유저: 유저가 신고한 유저 집합}
reportedCount - {유저: 신고당한 횟수}
*/

function solution(id_list, report, k) {
    var answer = Array(id_list.length).fill(0);
    var user = {};
    var reportTable = [];
    var reportUser = {};
    var reportedCount = {};
    for (i = 0; i < id_list.length; i ++) {
        user[id_list[i]] = i;
        reportTable.push(Array(id_list.length).fill(false));
        reportUser[id_list[i]] = [];
        reportedCount[id_list[i]] = 0;
    }
    
    for (i of report) {
        let tmp = i.split(" ");
        let reporter = tmp[0];
        let reported = tmp[1];
        
        if (reportTable[user[reporter]][user[reported]] === false) {
            reportedCount[reported] += 1;
            reportTable[user[reporter]][user[reported]] = true;
            reportUser[reporter].push(reported);
        }
    }
    
    for (i = 0; i < id_list.length; i ++) {
        if (reportedCount[id_list[i]] >= k) {
            for (j = 0; j < id_list.length; j ++) {
                if (reportTable[j][i] === true) {
                    answer[j] += 1;
                }
            }
        }
    }
    
    return answer;
}