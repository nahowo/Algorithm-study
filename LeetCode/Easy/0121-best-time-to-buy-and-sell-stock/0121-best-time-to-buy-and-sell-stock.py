class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=0
        answer=0
        for i in range(1,len(prices)):
            sell=i
            profit=prices[sell]-prices[buy]
            if prices[buy]<prices[sell]:
                answer=max(profit,answer)
            else:
                buy=sell
        
        return answer