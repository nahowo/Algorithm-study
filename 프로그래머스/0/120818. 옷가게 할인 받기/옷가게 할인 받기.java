class Solution {
    public int solution(int price) {
        int answer = 0;
        int percent = 0;
        if (price >= 500000) {
            percent = 20;
        } else if (price >= 300000) {
            percent = 10;
        } else if (price >= 100000) {
            percent = 5;
        }
        answer = price * (100 - percent) / 100;
        return answer;
    }
}