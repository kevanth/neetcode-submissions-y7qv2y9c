class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        ret = 0
        i = 0
        j = 0
        while i < len(prices):
            if prices[i] < lowest:
                lowest = prices[i]
            else:
                print(lowest, prices[i])
                ret = max(ret, prices[i]-lowest)
            i+=1
        return ret