# Earnings Yield Calculator
# -------------------------
# Overview:
# The Earnings Yield is a financial metric that indicates how much a company earns for each dollar of its stock price.
# It's essentially the inverse of the Price-to-Earnings (P/E) ratio.
#
# Formula:
# Earnings Yield = Earnings per Share (EPS) / Price per Share
#
# Desired Value:
# A higher Earnings Yield can indicate that a stock is undervalued and may represent a better value to investors.
# A lower Earnings Yield may suggest that a stock is overvalued relative to its earnings.
# 
# Note: This script uses hard-coded values for demonstration. For real-world applications, 
# actual financial data values should be input.

# Convert amounts where 1 million dollars is represented as 1.00, 10 million as 10.00, etc.
def convert_to_actual_value(value_in_millions):
    return value_in_millions * 1000000

# Hard-coded values

# Earnings Yield Calculator with Industry Comparisons and Contextual Information
def convert_to_actual_value(value_in_millions):
    """Convert amounts where 1 million dollars is represented as 1.00, 10 million as 10.00, etc."""
    return value_in_millions * 1000000

# Hard-coded values for the company
eps_in_millions = 2.74  # Example: $2.74 million
eps = convert_to_actual_value(eps_in_millions)
price_per_share_in_millions = 11.48  # Example: $11.48 million
price_per_share = convert_to_actual_value(price_per_share_in_millions)

# Hard-coded values for industry average
industry_avg_eps_in_millions = 2.20  # Example: $2.20 million
industry_avg_eps = convert_to_actual_value(industry_avg_eps_in_millions)
industry_avg_price_per_share_in_millions = 10.00  # Example: $10 million
industry_avg_price_per_share = convert_to_actual_value(industry_avg_price_per_share_in_millions)

# Calculate Earnings Yield
earnings_yield = eps / price_per_share
industry_avg_earnings_yield = industry_avg_eps / industry_avg_price_per_share

print(f"Company's Earnings Yield: {earnings_yield:.2%}")
print(f"Industry Average Earnings Yield: {industry_avg_earnings_yield:.2%}")

# Interpretation
if earnings_yield > industry_avg_earnings_yield:
    print("The company's Earnings Yield is higher than the industry average, suggesting it might be undervalued.")
    print("Factors and Scenarios Affecting the Ratio:")
    print("1. Strong Earnings: The company may be generating higher earnings, which increases the yield.")
    print("2. Market Underestimation: The market might be underestimating the company's growth prospects.")
elif earnings_yield < industry_avg_earnings_yield:
    print("The company's Earnings Yield is lower than the industry average, indicating it might be overvalued.")
    print("Factors and Scenarios Affecting the Ratio:")
    print("1. Market Hype: High demand for the stock may be driving up the price, reducing the earnings yield.")
    print("2. Declining Earnings: The company might be experiencing lower earnings which reduces the yield.")
else:
    print("The company's Earnings Yield is on par with the industry average.")
    print("Factors and Scenarios Affecting the Ratio:")
    print("1. Market Conformity: The stock is priced in line with industry expectations.")
    print("2. Stable Earnings: The company's earnings are consistent with industry norms.")
