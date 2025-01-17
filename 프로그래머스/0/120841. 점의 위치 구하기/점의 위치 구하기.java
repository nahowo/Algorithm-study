class Solution {
    public boolean isPos(int dot) {
        if (dot > 0) {
            return true;
        }
        return false;
    }
    
    public int solution(int[] dot) {
        int answer = 0;
        int x = dot[0];
        int y = dot[1];
        if (isPos(x)) {
            if (isPos(y)) {
                answer = 1;
            } else {
                answer = 4;
            }
        } else {
            if (isPos(y)) {
                answer = 2;
            } else {
                answer = 3;
            }
        }
        return answer;
    }
}