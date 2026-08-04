# Last updated: 8/4/2026, 10:00:16 AM
1class Solution(object):
2    def countDigits(self, num):
3        digits = [int(d) for d in str(num)]
4        c = 0
5        for digit in digits:
6            if num % digit == 0:
7                c += 1
8        return c
9        