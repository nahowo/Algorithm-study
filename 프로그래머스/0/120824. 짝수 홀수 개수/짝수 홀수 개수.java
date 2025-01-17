class Solution {
    public int isEven(int num) {
        if (num % 2 == 0) {
            return 0;
        }
        return 1;
    }
    
    public int[] solution(int[] num_list) {
        int[] answer = {0, 0};
        for (int i = 0; i < num_list.length; i ++) {
            answer[isEven(num_list[i])] += 1;
        }
        return answer;
    }
}