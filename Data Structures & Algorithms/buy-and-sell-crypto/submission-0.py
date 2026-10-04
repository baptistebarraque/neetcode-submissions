class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        min_left=prices[0]
        for i in range(len(prices)):
            if prices[i]-min_left>max_profit:
                max_profit=prices[i]-min_left
            if min_left>prices[i]:
                min_left=prices[i]
        return max_profit


        