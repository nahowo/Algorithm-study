class Solution {
    public boolean isGCD(String x, String str) {
        boolean answer = true;
        if (str.length() % x.length() != 0) {
            answer = false;
        } else {
            for (int i = 0; i < str.length(); i ++) {
                if (str.charAt(i) != x.charAt(i % x.length())) {
                    answer = false;
                    break;
                }
            }
        }
        return answer;
    }

    public String gcdOfStrings(String str1, String str2) {
        String x = "";
        String tmpx = "";
        int len1 = str1.length();
        int len2 = str2.length();

        for (int i = 0; i < Math.min(len1, len2); i ++) {
            if (str1.charAt(i) == (str2.charAt(i))) {
                tmpx += str1.charAt(i);
                if (isGCD(tmpx, str1) && isGCD(tmpx, str2)) {
                    x = tmpx;
                }
            }
        }
        return x;
    }
}