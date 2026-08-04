# Last updated: 8/4/2026, 10:04:27 AM
1class Solution(object):
2    def isPalindrome(self, x):
3        temp = str(x)
4        if (temp == temp[::-1]):
5            return True
6        else: 
7            return False
8             
9        