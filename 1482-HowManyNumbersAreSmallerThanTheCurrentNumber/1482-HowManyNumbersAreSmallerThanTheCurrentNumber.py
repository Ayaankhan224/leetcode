# Last updated: 8/4/2026, 4:05:34 PM
class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        answer = []
        for i in nums:
            c = 0
            for j in nums:
                if j<i:
                    c += 1
            answer.append(c)
        
        return answer