class Solution {
    public int getMul(int[] arr) {
        int s = 1;
        for (int i: arr) {
            s *= i;
        }
        return s;
    }
    
    public int getSumSquare(int[] arr) {
        int s = 0;
        for (int i: arr) {
            s += i;
        }
        return s * s;
    }
    
    public int solution(int[] num_list) {
        if (getMul(num_list) < getSumSquare(num_list)) {
            return 1;
        }
        return 0;
    }
}