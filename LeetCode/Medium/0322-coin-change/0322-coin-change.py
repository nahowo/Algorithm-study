class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        m=10**4+1
        dp=[m]*(amount+1)
        dp[0]=0
        for i in range(amount+1):
            for j in coins:
                if i-j>=0:
                    dp[i]=min(dp[i],dp[i-j]+1)
        if dp[amount]>=m:
            return -1
        else:
            return dp[amount]