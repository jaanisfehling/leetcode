class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        h = len(x)//2
        return x[:h][::-1] == x[h:] or x[:h][::-1] == x[h+1:]
