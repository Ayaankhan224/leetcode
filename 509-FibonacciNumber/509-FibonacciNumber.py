# Last updated: 8/8/2026, 9:43:45 AM
1class Solution(object):
2    def fib(self, n):
3        if n==0 or n==1:
4            return n
5        else:
6            return self.fib(n-1) + self.fib(n-2)        