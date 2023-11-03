# Graham Number Calculation
# -------------------------
# Overview:
# The Graham Number is a metric that provides an estimate of a stock's maximum fair price.
# It's derived from the book value per share and the earnings per share (EPS).
#
# Desired Value:
# A higher Graham Number relative to the current stock price may indicate that the stock is undervalued. 
# Conversely, if the stock price is significantly higher than the Graham Number, 
# it could suggest overvaluation.

import math

# Hardcoded values (in the format where 1 million is represented as 1.00, etc.)
book_value_per_share = 5.00  # For example, $5 million
earnings_per_share = 2.50   # For example, $2.5 million

def calculate_graham_number(bvps, eps):
    """Calculate the Graham Number based on book value per share and earnings per share."""
    return math.sqrt(22.5 * bvps * eps)

graham_number = calculate_graham_number(book_value_per_share, earnings_per_share)

# Output the result and its implications
print(f"Graham Number: ${graham_number:.2f} million")
print("--------- Factors and Scenarios Affecting the Graham Number ---------")

# Discussing Influencing Factors and Scenarios
print("1. Book Value Per Share:")
print("   - A low BVPS might be due to excessive liabilities or recent write-offs.")
print("   - A high BVPS could indicate undervaluation, especially if it is growing over the years.")

print("\n2. Earnings Per Share (EPS):")
print("   - A low EPS could be indicative of poor profitability.")
print("   - A high EPS generally implies strong profitability, but also verify if this is consistent over time.")

print("\n3. Market Conditions:")
print("   - In a bear market, investors might ignore fundamentals, making the Graham Number less effective.")
print("   - In a bull market, a lower Graham Number compared to stock price could indicate overheating.")

print("\n4. Business Lifecycle:")
print("   - For startups or high-growth companies, the Graham Number may underestimate the fair value.")
print("   - For stable, mature companies, the Graham Number can be a more reliable indicator.")

print("\n5. Asset Quality:")
print("   - Non-performing assets or low-quality investments can artificially inflate the BVPS.")
print("   - Ensure the quality of assets and liabilities when interpreting the Graham Number.")