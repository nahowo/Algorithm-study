class Solution {
    public int pow(int n, int i) {
        int result = 1;
        for (int idx = 0; idx < i; idx ++) {
            result *= n;
        }
        return result;
    }
    
    public int solution(int a, int b, int c) {
        int answer = a + b + c;
        if (a == b && b == c) {
            answer *= (pow(a, 2) + pow(b, 2) + pow(c, 2)) * (pow(a, 3) + pow(b, 3) + pow(c, 3));
        }
        else if (a == b || b == c || c == a) {
            answer *= (pow(a, 2) + pow(b, 2) + pow(c, 2));
        }
        return answer;
    }
}