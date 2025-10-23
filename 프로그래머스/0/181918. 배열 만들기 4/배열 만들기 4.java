import java.util.*;

class Solution {
    public int[] solution(int[] arr) {
        int[] answer = {};
        
        ArrayList<Integer> stk = new ArrayList<>();
        int i = 0;
        while (i < arr.length) {
            if (stk.size() == 0) {
                stk.add(arr[i]);
                i += 1;
            } else {
                if (stk.get(stk.size() - 1) < arr[i]) {
                    stk.add(arr[i]);
                    i += 1;
                } else {
                    stk.remove(stk.size() - 1);
                }
            }
        }
        answer = stk.stream().mapToInt(Integer::intValue).toArray();
        return answer;
    }
}