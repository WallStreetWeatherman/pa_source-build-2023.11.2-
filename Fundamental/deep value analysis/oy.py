# Owner's Yield Calculator
#
# Overview:
# The Owner's Yield metric combines both the dividend yield and the buyback yield 
# to provide a more comprehensive perspective on shareholder return. It encompasses 
# the total return a shareholder might expect from both dividends and stock repurchases.
#
# Desired Value:
# A higher Owner's Yield generally suggests better shareholder return. Conversely, 
# a low Owner's Yield could indicate less return to shareholders from dividends 
# and buybacks combined.

def owners_yield(annual_dividends, shares_bought_back, current_share_price, market_cap_in_millions):
    # Convert market cap to the desired format (1 million as 1.00)
    market_cap = market_cap_in_millions * 1_000_000

    # Calculate Dividend Yield
    dividend_yield = annual_dividends / market_cap

    # Calculate Buyback Yield
    buyback_value = shares_bought_back * current_share_price
    buyback_yield = buyback_value / market_cap

    # Calculate Owner's Yield
    total_yield = dividend_yield + buyback_yield

    return total_yield

# Hardcoded example values
annual_dividends = 10_000_000  # Example: $10 million in dividends paid out
shares_bought_back = 1_000_000  # Example: 1 million shares bought back
current_share_price = 50  # Example: Current share price is $50
market_cap_in_millions = 500.00  # Example: $500 million market cap (represented as 500.00)

oy = owners_yield(annual_dividends, shares_bought_back, current_share_price, market_cap_in_millions)
print(f"Owner's Yield: {oy:.2%}")
