class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b = 0
        s = 1 if len(prices) >= 2 else 0
        ret = max(0, prices[s] - prices[b])
        for i in range(1,len(prices)):
            if prices[i] < prices[b]:
                b = i
                if s<b:
                    s = b+1
            else:
                s +=1
            if s>=len(prices):
                break
            ret = max(ret, prices[s] - prices[b])
            print(prices[b], prices[s], ret)
        return ret