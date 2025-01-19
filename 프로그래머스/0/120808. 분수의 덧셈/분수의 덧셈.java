class Solution {
    public int[] solution(int numer1, int denom1, int numer2, int denom2) {
        int[] answer = {0, 0};
        int numer = numer1 * denom2 + numer2 * denom1;
        int denom = denom1 * denom2;
        answer[0] = numer;
        answer[1] = denom;
        
        for (int div = Math.min(numer, denom); div > 1; div --) {
            if ((numer % div == 0) && (denom % div == 0)) {
                answer[0] = numer / div;
                answer[1] = denom / div;
                break;
            }
        }
        
        return answer;
    }
}