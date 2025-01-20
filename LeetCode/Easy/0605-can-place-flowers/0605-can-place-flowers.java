class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        boolean result = false;
        int len = flowerbed.length;

        for (int i = 0; i < len; i ++) {
            if (flowerbed[i] == 0) {
                boolean flag = true;
                if (i - 1 >= 0) {
                    if (flowerbed[i - 1] == 1) {
                        flag = false;
                    }
                }
                if (i + 1 < len) {
                    if (flowerbed[i + 1] == 1) {
                        flag = false;
                    }
                }
                if (flag) {
                    flowerbed[i] = 1;
                    n -= 1;
                }
            }
        }

        if (n <= 0) {
            result = true;
        }
        return result;
    }
}
