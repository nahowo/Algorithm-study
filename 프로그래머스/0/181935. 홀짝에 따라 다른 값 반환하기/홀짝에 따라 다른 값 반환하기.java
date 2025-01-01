class Solution {
    public int pow(int n, int cnt) {
        int result = 1;
        for (int i = 0; i < cnt; i ++) {
            result *= n;
        }
        return result;
    }
    
    public int getSum(int n, int type) {
        int sum = 0;
        for (int i = type; i <= n; i += 2) {
            sum += pow(i, (2 - type));
        }
        return sum;
    }
    
    public int getOddSum(int n) {
        int sum = 0;
        for (int i = 1; i <= n; i += 2) {
            sum += i;
        }
        return sum;
    }
    
    public int solution(int n) {
        int answer;
        answer = getSum(n, n % 2);
        return answer;
    }
}