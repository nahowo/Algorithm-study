class Solution {
    public int[] solution(int n) {
        int len = len = (n + 1) / 2;
        int[] answer = new int[len];
        int idx = 0;
        for (int i = 1; i <= n; i ++) {
            if (i % 2 == 1) {
                answer[idx] = i;
                idx ++;
            }
        }
        return answer;
    }
}