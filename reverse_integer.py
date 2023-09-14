class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        if x[0] == "-":
            res = int("-" + x[1:][::-1])
            return res if res <= 2**31 -1 and res >= -2**31 else 0
        else:
            res = int(x[::-1])
            return res if res <= 2**31 -1 and res >= -2**31 else 0

        
