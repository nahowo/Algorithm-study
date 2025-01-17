class Solution {    
    public int solution(String str1, String str2) {
        int answer = 2;
        int l1 = str1.length();
        int l2 = str2.length();
        
        for (int i1 = 0; i1 < l1 - l2 + 1; i1 ++) {
            int i2 = 0;
            boolean flag = true;
            if (str1.charAt(i1) == str2.charAt(i2)) {
                for (i2 = 0; i2 < l2; i2 ++) {
                    if (str1.charAt(i1 + i2) != str2.charAt(i2)) {
                        flag = false;
                        break;
                    }
                }
                if (flag) {
                    answer = 1;
                    break;
                }
            }
        }
        return answer;
    }
}