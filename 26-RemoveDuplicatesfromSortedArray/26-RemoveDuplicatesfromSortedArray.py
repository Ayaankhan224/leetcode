# Last updated: 8/8/2026, 6:31:48 PM
1class Solution:
2    def removeDuplicates(self, nums: List[int]) -> int:
3        start = 0
4        for i in range(1,len(nums)):
5            if nums[i] != nums[start]:
6                start += 1
7                nums[start] = nums[i]
8
9        return start+1