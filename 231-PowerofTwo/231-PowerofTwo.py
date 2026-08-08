# Last updated: 8/8/2026, 10:02:56 AM
1class Solution(object):
2    def isPowerOfTwo(self, n):
3        if n<=0:
4            return False
5        while n%2==0:
6            n//=2
7        return n==1
8            
9        