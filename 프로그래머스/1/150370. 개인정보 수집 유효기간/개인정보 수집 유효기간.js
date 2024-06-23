function isExpired(today, term, collectedAt) {
    tTmp = today.split(".");
    tYear = Number(tTmp[0]);
    tMonth = Number(tTmp[1]);
    tDay = Number(tTmp[2]);
    
    cTmp = collectedAt.split(".");
    cYear = Number(cTmp[0]);
    cMonth = Number(cTmp[1]);
    
    if (cMonth + term > 12) {
        exYear = cYear + Math.floor((cMonth + term) / 12);
        exMonth = (cMonth + term) % 12;
    } else {
        exYear = cYear;
        exMonth = cMonth + term;
    }
    exDay = Number(cTmp[2]) - 1;
    
    if (exDay == 0) {
        exDay = 28;
        exMonth -= 1;
    }
    if (exMonth == 0) {
        exMonth = 12;
        exYear -= 1;
    }
    console.log("today is "+tYear+"."+tMonth+"."+tDay);
    console.log("expired at "+exYear+"."+exMonth+"."+exDay);
    
    if (tYear > exYear) {
        return true;
    } else if (tYear === exYear) {
        if (tMonth > exMonth) {
            return true;
        } else if (tMonth === exMonth) {
            if (tDay > exDay) {
                return true;
            }
        }
    }
    return false;
}

function solution(today, terms, privacies) {
    var answer = [];
    var termDict = {};
    for (i = 0; i < terms.length; i ++) {
        let tmp = terms[i].split(" ");
        termDict[tmp[0]] = Number(tmp[1]);
    }
    
    for (i = 0; i < privacies.length; i ++) {
        let tmp = privacies[i].split(" ");
        let collectedAt = tmp[0];
        let term = termDict[tmp[1]];
        let result = isExpired(today, term, collectedAt);
        if (result === true) {
            answer.push(i+1);
        }
    }
    return answer;
}