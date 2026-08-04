# Last updated: 8/4/2026, 9:52:00 AM
1class Solution(object):
2    def smallerNumbersThanCurrent(self, nums):
3        answer = []
4        for i in nums:
5            c = 0
6            for j in nums:
7                if j<i:
8                    c += 1
9            answer.append(c)
10        
11        return answer