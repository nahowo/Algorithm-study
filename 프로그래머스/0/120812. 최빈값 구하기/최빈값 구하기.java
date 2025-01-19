import java.util.HashMap;
import java.util.Map;

class Solution {
    public int solution(int[] array) {
        int answer = 0;
        Map<Integer, Integer> dict = new HashMap<>();
        int maxCnt = 0;
        int maxNum = 0;
        
        for (int i = 0; i < array.length; i ++) {
            if (dict.containsKey(array[i])) {
                dict.put(array[i], dict.get(array[i]) + 1);
            } else {
                dict.put(array[i], 1);
            }
            if (dict.get(array[i]) > maxCnt) {
                maxCnt = dict.get(array[i]);
                maxNum = array[i];
            }
        }
        
        answer = maxNum;
        for (int i = 0; i < array.length; i ++) {
            if (dict.get(array[i]) == maxCnt && array[i] != maxNum) {
                answer = -1;
            }
        }
        
        return answer;
    }
}