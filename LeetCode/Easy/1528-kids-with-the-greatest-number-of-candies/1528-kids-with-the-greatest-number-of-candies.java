class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        int n = candies.length;
        List<Boolean> result = new ArrayList<>();
        int maxCnt = 0;

        for (int i = 0; i < n; i ++) {
            if (candies[i] > maxCnt) {
                maxCnt = candies[i];
            }
        }

        for (int i = 0; i < n; i ++) {
            if (candies[i] + extraCandies >= maxCnt) {
                result.add(i, true);
            } else {
                result.add(i, false);
            }
        }
        return result;
    }
}
