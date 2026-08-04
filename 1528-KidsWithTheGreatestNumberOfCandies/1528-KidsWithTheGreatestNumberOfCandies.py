# Last updated: 8/4/2026, 4:05:36 PM
class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        res = []
        for i in candies:
            if (i+extraCandies) >= max(candies):
                res.append(True)
            else:
                res.append(False)
        
        return res