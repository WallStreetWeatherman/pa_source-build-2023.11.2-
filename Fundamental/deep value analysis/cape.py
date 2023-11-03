# CAPE (Cyclically Adjusted Price to Earnings) Ratio Calculation
# --------------------------------------------------------------
# Overview:
# The CAPE Ratio, developed by Robert Shiller, is a valuation measure that uses real earnings 
# per share (EPS) over a 10-year period. This smoothes out the cyclical fluctuations in corporate profits.
# By considering a 10-year window, the CAPE Ratio offers a long-term perspective on a company's valuation.
#
# Desired Value:
# Generally, a lower CAPE suggests the stock may be undervalued relative to its historical trend,
# but this needs to be compared to the broader market or its industry peers. A high CAPE indicates
# potential overvaluation, suggesting caution.

# Hardcoded values (using the format where 1 million is represented as 1.00, etc.)
current_price = 50.00  # Company's current stock price (e.g., $50 million)
average_10_year_eps = 4.00  # Average real EPS over the past 10 years (e.g., $4 million)

# Calculate CAPE Ratio
def calculate_cape(price, avg_10_year_eps):
    """Calculate CAPE Ratio."""
    return price / avg_10_year_eps

cape_ratio = calculate_cape(current_price, average_10_year_eps)

print(f"CAPE Ratio: {cape_ratio:.2f}")

# Interpretation
# Note: Historical averages for the CAPE Ratio vary over time and between markets. 
# For illustrative purposes, let's consider 20 as a historical average benchmark.
benchmark = 20.0  
if cape_ratio < benchmark:
    print(f"The company's CAPE Ratio is below the historical average, indicating potential undervaluation.")
elif cape_ratio == benchmark:
    print(f"The company's CAPE Ratio aligns with the historical average.")
else:
    print(f"The company's CAPE Ratio is above the historical average, suggesting potential overvaluation and the need for caution.")
