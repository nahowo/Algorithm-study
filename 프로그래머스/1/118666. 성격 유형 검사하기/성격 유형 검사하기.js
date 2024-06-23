/*
문항 정보 + 선택 정보 순회
    if 선택 정보가 1~3인 경우
        문항 정보[0] 유형값 += 가중치
    if 선택 정보가 5~7인 경우
        문항 정보[1] += 가중치
*/

function score(problem, pick) {
    var type = problem[Math.floor(pick / 4)];
    var point = Math.abs(4 - pick);
    return [type, point];
}

function solution(survey, choices) {
    var answer = '';
    var type = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0};
    
    for (i = 0; i < survey.length; i ++) {
        var tmp = score(survey[i], choices[i]);
        type[tmp[0]] += tmp[1];
    }
    
    if (type['R'] < type['T']) {
        answer += 'T';
    } else {
        answer += 'R';
    }
    if (type['C'] < type['F']) {
        answer += 'F';
    } else {
        answer += 'C';
    }
    if (type['J'] < type['M']) {
        answer += 'M';
    } else {
        answer += 'J';
    }
    if (type['A'] < type['N']) {
        answer += 'N';
    } else {
        answer += 'A';
    }
    return answer;
}