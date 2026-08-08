# Last updated: 8/8/2026, 7:01:10 PM
1class Solution:
2    def maxSubArray(self, nums: List[int]) -> int:
3        currSum = 0
4        maxSum = nums[0]
5        for i in range(len(nums)):
6            currSum += nums[i]
7            maxSum = max(maxSum, currSum)
8            if currSum < 0:
9                currSum = 0
10        
11        return maxSum