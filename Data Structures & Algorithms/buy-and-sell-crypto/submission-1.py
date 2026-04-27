class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # idx2=0
        # max_profit=0
        # for idx in range(len(prices)):
        #     if prices[idx] > prices[idx2]:
        #         profit= profit[idx]- profit[idx2]
        #         max_profit= max(profit, max_profit)
        #         idx2= idx
        # return max_profit
        max_profit=0
        for i in range(len(prices)):
            max_profit_loop=0
            for j in range(i+1, len(prices)):
                if prices[j]>prices[i]:
                    profit= prices[j]-prices[i]
                    max_profit_loop= max(profit, max_profit_loop)
            max_profit= max(max_profit, max_profit_loop)
        return max_profit