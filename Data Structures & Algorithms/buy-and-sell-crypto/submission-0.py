class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        i = 0
        if len(prices)==0 or len(prices)==1:
            return 0
        while i<len(prices)-1:
            j=i+1
            if prices[j]>prices[i]:
                while j<len(prices) and prices[j]>prices[i]:
                    j+=1
                    profit = max(profit,prices[j-1]-prices[i])
            i+=1
        return profit