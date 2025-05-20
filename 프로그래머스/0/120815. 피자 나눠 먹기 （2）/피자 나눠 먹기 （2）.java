class Solution {
    public int getGcd(int a, int b) {
        if (b == 0) {
            return a;
        }
        return getGcd(b, a % b);
    }
    
    public int solution(int n) {
        int answer = 0;
        int lmc = (6 * n) / getGcd(n, 6);
        answer = lmc / 6;
        return answer;
    }
}