class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0: return [0]
        ans = [0, 1]
        import math
        for k in range(2, n+1):
            counter = 0
            for j in range(int(math.log(k, 2)), -1, -1):
                num = 2**j
                if k - num >= 0:
                    k -= num
                    counter += 1


            ans.append(counter)
        return ans
                
