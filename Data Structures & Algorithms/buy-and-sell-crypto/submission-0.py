class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxCount = 0
        i,j=0,0
        while j<len(prices):
            if(prices[j]>prices[i]):
                maxCount = max(maxCount, prices[j]-prices[i])
            else:
                i=j
            j+=1
        return maxCount