function solution(a, b) {
    var answer = 0;
    tmp1 = Number(String(a) + String(b));
    tmp2 = 2*a*b;
    
    if ( tmp1 >= tmp2 ) {
        answer = tmp1;
    } else {
        answer = tmp2;
    }
    
    return answer;
}