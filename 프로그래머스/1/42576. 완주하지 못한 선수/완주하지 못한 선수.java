import java.util.HashMap;
import java.util.Map;

class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        Map<String, Integer> check = new HashMap<>();
        for (int i = 0; i < participant.length; i ++) {
            if (!check.containsKey(participant[i])) {
                check.put(participant[i], 1);
            } else {
                check.put(participant[i], check.get(participant[i]) + 1);
            }
        }
        for (int i = 0; i < completion.length; i ++) {
            check.put(completion[i], check.get(completion[i]) - 1);
        }
        for (int i = 0; i < participant.length; i ++) {
            if (check.get(participant[i]) > 0) {
                answer = participant[i];
                break;
            }
        }
        return answer;
    }
}