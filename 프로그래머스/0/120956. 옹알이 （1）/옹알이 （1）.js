function solution(babbling) {
    var answer = 0;
    for (let b of babbling) {
        answer += check(b);
    }
    return answer;
}

function check(word) {
    let l = word.length;
    word = word.replace(/aya/, "   ");
    word = word.replace(/ye/, "  ");
    word = word.replace(/woo/, "   ");
    word = word.replace(/ma/, "  ");
    
    const regexp = new RegExp(`\\s{${l}}`);
    if (word.match(regexp)) {
        return 1;
    }
    return 0;
}