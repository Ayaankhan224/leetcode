# Last updated: 8/4/2026, 4:05:32 PM
class Solution(object):
    def countDigits(self, num):
        digits = [int(d) for d in str(num)]
        c = 0
        for digit in digits:
            if num % digit == 0:
                c += 1
        return c
        