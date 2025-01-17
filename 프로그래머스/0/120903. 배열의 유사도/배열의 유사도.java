import java.util.HashSet;
import java.util.Arrays;

class Solution {
    public int solution(String[] s1, String[] s2) {
        int answer = 0;
        HashSet<String> h1 = new HashSet<>(Arrays.asList(s1));
        HashSet<String> h2 = new HashSet<>(Arrays.asList(s2));
        h1.retainAll(h2);
        answer = h1.size();
        
        return answer;
    }
}