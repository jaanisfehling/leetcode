class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1: return 0
        performance = prices[1] - prices[0]
        current_min = prices[0]

        for i in range(1, len(prices)):
            if prices[i] < current_min:
                current_min = prices[i]
            else:
                new_perf = prices[i] - current_min
                if new_perf > performance:
                    performance = new_perf

        return performance if performance > 0 else 0
