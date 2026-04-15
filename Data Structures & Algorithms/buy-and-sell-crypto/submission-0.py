class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        l = 0 # buy day
        r = 1 # sell day

        while r in range(len(prices)): # why range len prices and why len(prices)?
            if prices[r] > prices [l]:
                
                profit = max(profit, prices[r] - prices[l] )
            else:
                l = r
            r +=1

        return profit
            

