class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buy,sell= 0,1
        # max_profit=0
        # while sell<=len(prices)-1:
        #     if prices[sell]>=prices[buy]:
        #         max_profit= max(max_profit, prices[sell]-prices[buy])
        #     else:
        #         buy= sell
        #     sell+=1
        # return max_profit
        i,j=0,1
        max_profit=0
        while j< len(prices):
            if prices[j]<=prices[i]:
                i=j
            else:
                max_profit= max(max_profit, prices[j]-prices[i])
            j+=1
        return max_profit

