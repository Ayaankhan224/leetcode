# Last updated: 8/4/2026, 4:05:45 PM
class Solution(object):
    def subtractProductAndSum(self, n):
        digits = [int(digit) for digit in str(n)]
        pro = 1
        sum = 0
        for i in digits:
            pro *= i
            sum += i 
        
        return pro - sum