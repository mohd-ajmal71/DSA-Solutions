class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        current_profit = 0
        max_profit = 0
        for p in prices:
            if p < min_price:
                min_price = p
            current_profit = p - min_price
            if max_profit < current_profit:
                max_profit = current_profit

        return max_profit


