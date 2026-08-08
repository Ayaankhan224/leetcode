# Last updated: 8/8/2026, 6:13:29 PM
1class Solution(object):
2    def runningSum(self, nums):
3        op = []
4        temp = 0
5        for i in range(len(nums)):
6            temp += nums[i]
7            op.append(temp)
8        return op