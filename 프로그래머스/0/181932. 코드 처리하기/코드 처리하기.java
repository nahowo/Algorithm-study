class Solution {
    static int mode = 0;
    
    public void chmod() {
        mode = (mode + 1) % 2;
    }
    
    public String solution(String code) {
        String ret = "";
        for (int idx = 0; idx < code.length(); idx ++) {
            if (code.charAt(idx) == '1') {
                chmod();
            } else {
                if (idx % 2 == mode) {
                    ret += code.charAt(idx);
                }
            }
        }
        if (ret.equals("")) {
            return "EMPTY";
        }
        return ret;
    }
}