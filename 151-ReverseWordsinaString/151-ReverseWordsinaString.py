# Last updated: 8/9/2026, 5:51:18 PM
1class Solution:
2    def reverseWords(self, s: str) -> str:
3        words = s.split()
4        words.reverse()
5        return " ".join(words)
6        
7