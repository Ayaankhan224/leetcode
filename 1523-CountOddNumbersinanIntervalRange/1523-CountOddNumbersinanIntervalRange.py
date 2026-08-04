# Last updated: 8/4/2026, 9:42:54 AM
1class Solution(object):
2    def countOdds(self, low, high):
3        return (high+1)//2 - (low//2)
4        