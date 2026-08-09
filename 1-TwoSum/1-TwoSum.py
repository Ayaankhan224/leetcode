# Last updated: 8/9/2026, 7:52:38 PM
1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3        dict1 = {}
4        for i in range(len(nums)):
5            rem = target - nums[i]
6            if rem in dict1:
7                return [dict1[rem], i]
8            dict1[nums[i]] = i
9