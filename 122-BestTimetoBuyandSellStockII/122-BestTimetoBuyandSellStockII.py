# Last updated: 8/9/2026, 7:58:28 AM
1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        profit = 0
4        for i in range(1, len(prices)):
5            if prices[i] > prices[i-1]:
6                profit += prices[i] - prices[i-1]
7
8        return profit
9
10