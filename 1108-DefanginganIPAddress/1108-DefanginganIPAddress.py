# Last updated: 8/9/2026, 8:13:00 AM
1class Solution:
2    def defangIPaddr(self, address: str) -> str:
3        return address.replace(".","[.]")