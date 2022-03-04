stock_prices = [10, 7, 5, 8, 11, 9]

def get_max_profit(stock_prices):
    min_price = stock_prices[0]
    if len(stock_prices) < 2:
        return("Finding stock prices requires 2 values.")

    max_profit = stock_prices[1] - stock_prices[0]

    for current_time in xrange(1, len(stock_prices)):
        current_price = stock_prices[current_time]
        
        potential_profit = current_price-min_price
        max_profit = max(max_profit,potential_profit)
        min_price = min(min_price,current_price)
        
    return max_profit

print(get_max_profit(stock_prices))
# Returns 6 (buying for $5 and selling for $11)
