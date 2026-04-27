class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        for idx1 in range(len(prices)):
            for idx2 in range(idx1+1, len(prices)): 
                if prices[idx2]>prices[idx1]:
                    max_profit= max(max_profit, prices[idx2]-prices[idx1])
        return max_profit