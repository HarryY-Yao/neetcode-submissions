class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        max_profit = 0

        while l < len(prices) - 1:
            curr_profit = 0
            while r < len(prices) and curr_profit >= 0:
                curr_profit = prices[r] - prices[l]
                print(curr_profit)
                max_profit = max(max_profit, curr_profit)
                r += 1
            
            l = r - 1

        return max_profit