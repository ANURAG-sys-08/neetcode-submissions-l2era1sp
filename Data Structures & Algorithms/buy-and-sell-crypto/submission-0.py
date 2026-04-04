class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_elem = prices[0]
        for i in range(len(prices)-1):
            min_elem = min(min_elem,prices[i+1])
            profit = prices[i+1] - min_elem
            max_profit = max(max_profit,profit)
        return max_profit