class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i, buy_num in enumerate(prices[:-1]):
            for sell_num in prices[i+1:]:
                if buy_num < sell_num:
                    res = max(res, sell_num-buy_num)
        return res

        