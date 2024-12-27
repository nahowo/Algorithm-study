class Solution {
    public long solution(int a, int b) {
        long answer = 0;
        if (a > b) { // a <= b 유지
            int tmp = b;
            b = a;
            a = tmp;
        }
        
        long sum = (long)a + (long)b;
        long cnt = (long)b - (long)a;
        
        if ((b - a) % 2 == 0) { // a ~ b 사이 정수의 개수가 홀수
            answer += sum * cnt / 2 + sum / 2;
        }
        else { // a ~ b 사이 정수의 개수가 짝수
            answer += sum * (cnt + 1) / 2;
        }
        return answer;
    }
}