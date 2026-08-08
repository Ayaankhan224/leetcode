# Last updated: 8/8/2026, 6:47:20 PM
1class Solution:
2    def sortArrayByParity(self, nums: List[int]) -> List[int]:
3        ev = []
4        od = []
5        nums.sort()
6        for i in nums:
7            if i%2==0:
8                ev.append(i)
9            else:
10                od.append(i)
11        return ev+od