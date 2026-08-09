# Last updated: 8/9/2026, 8:04:14 AM
1class Solution:
2    def maximumWealth(self, accounts: List[List[int]]) -> int:
3        wealth = 0
4        for i in range(len(accounts)):
5            temp = 0
6            for j in accounts[i]:
7                temp += j
8                if temp > wealth:
9                    wealth = temp
10        
11        return wealth