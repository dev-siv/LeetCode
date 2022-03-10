def maxProfit(prices):
    left = 0
    right = 1
    max_profit = 0
    while right < len(prices):
        if prices[right] > prices[left]:
            profit = prices[right] - prices[left]
            if profit > max_profit:
                max_profit = profit
        else:
            left = right
        right += 1
    return max_profit


def maxProfit2(prices):
    max_profit, min_price = 0, float('inf')
    for price in prices:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(max_profit, profit)
    return max_profit


if __name__ == "__main__":
    nums = [7, 1, 5, 3, 6, 4]
    print(maxProfit(nums))
    n = [7, 6, 4, 3, 1]
    print(maxProfit(n))
    print(maxProfit2(n))
