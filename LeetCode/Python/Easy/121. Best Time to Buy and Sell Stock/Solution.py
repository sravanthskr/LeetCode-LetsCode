class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowPrice=prices[0]
        maxProfit=0
        for i in range(len(prices)):
            if lowPrice>prices[i]:
                lowPrice=prices[i] # need least, minimum
            else:
                profit=prices[i]-lowPrice
                if profit>maxProfit:
                    maxProfit=profit
        return maxProfit