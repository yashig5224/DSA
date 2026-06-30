class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # Edge case: if prices list is empty
        if not prices:
            return 0
            
        max_profit = 0
        best_buy = prices[0]

        # Iterate through prices starting from index 1
        for i in range(1, len(prices)):
            if prices[i] > best_buy:
                max_profit = max(max_profit, prices[i] - best_buy)
                
            best_buy = min(best_buy, prices[i])

        return max_profit
