# Last updated: 8/4/2026, 4:05:30 PM
class Solution(object):
    def countOdds(self, low, high):
        return (high+1)//2 - (low//2)
        