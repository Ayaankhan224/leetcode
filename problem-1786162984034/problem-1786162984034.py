# Last updated: 8/8/2026, 9:53:04 AM
1class Solution(object):
2    def tribonacci(self, n):
3        if n==0:
4            return 0
5        elif n==1 or n==2:
6            return 1
7        a = 0
8        b = 1
9        c = 1
10        for i in range(3,n+1):
11            d = a+b+c
12            a = b
13            b = c
14            c = d
15        return c
16        