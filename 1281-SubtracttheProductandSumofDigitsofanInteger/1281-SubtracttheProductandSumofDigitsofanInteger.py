# Last updated: 8/4/2026, 3:58:46 PM
1class Solution(object):
2    def subtractProductAndSum(self, n):
3        digits = [int(digit) for digit in str(n)]
4        pro = 1
5        sum = 0
6        for i in digits:
7            pro *= i
8            sum += i 
9        
10        return pro - sum