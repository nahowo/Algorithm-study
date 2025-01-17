class Solution {
    public int solution(int[] sides) {
        int answer = 1;
        int maxIdx = 0;
        int maxNum = 0;
        for (int i = 0; i < 3; i ++) {
            if (maxNum < sides[i]) {
                maxNum = sides[i];
                maxIdx = i;
            }
        }
        
        if (maxNum >= sides[(maxIdx + 1) % 3] + sides[(maxIdx + 2) % 3]) {
            answer = 2;
        }
        return answer;
    }
}