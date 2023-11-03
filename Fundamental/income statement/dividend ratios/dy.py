# Dividend Yield Calculator
# -------------------------
# Overview:
# The Dividend Yield is a financial metric that indicates how much a company pays out in dividends 
# each year relative to its stock price. It's a way to measure the return on investment for a stock 
# based solely on dividends.
#
# Formula:
# Dividend Yield = Annual Dividends per Share / Price per Share
#
# Desired Value:
# A high Dividend Yield can indicate that a stock provides a good return on investment through dividends, 
# or it might indicate that the stock price has decreased. A low Dividend Yield can indicate the opposite 
# or that the company is reinvesting its profits instead of paying them out as dividends.
# 
# Note: This script uses hard-coded values for demonstration. For real-world applications, 
# actual financial data values should be input.

# Convert amounts where 1 million dollars is represented as 1.00, 10 million as 10.00, etc.
def convert_to_actual_value(value_in_millions):
    return value_in_millions * 1000000

# Hard-coded values

# Annual Dividends per Share (This is usually in dollars and cents, so no conversion needed here)
annual_dividends_per_share = 5.00  # Example value representing $5.00 dividend per share

# Price per Share (in million dollars format for simplicity, though this is a high value for a stock price)
price_per_share_in_millions = 0.10  # Example value representing $100,000 for a share price (this is unrealistic in practice, but for the sake of demonstration)
price_per_share = convert_to_actual_value(price_per_share_in_millions)

# Calculate Dividend Yield
dividend_yield = annual_dividends_per_share / price_per_share

# Output the results
print(f"Dividend Yield: {dividend_yield:.2%}")

if dividend_yield > 0.05:  # 5% as a threshold
    print("The stock has a high Dividend Yield, which might make it attractive to income-oriented investors.")
else:
    print("The stock has a low Dividend Yield, which could mean the company is reinvesting its profits or that the stock price is high relative to the dividend payout.")
