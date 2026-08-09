# Last updated: 8/9/2026, 7:45:09 AM
1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        min_price = prices[0]
4        profit = 0
5        
6        for i in range(1, len(prices)):
7            if prices[i] < min_price:
8                min_price = prices[i]
9            else:
10                temp = prices[i] - min_price
11                if temp > profit:
12                    profit = temp
13        
14        return profit