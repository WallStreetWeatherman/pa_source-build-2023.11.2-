# Return on Invested Capital (ROIC) Calculator
# --------------------------------------------
# Overview:
# Return on Invested Capital (ROIC) is a measure used to assess a company's efficiency at allocating 
# the capital under its control to profitable investments. It gives a sense of how well a company is 
# using its money to generate returns.
#
# Formula:
# ROIC = NOPAT / Invested Capital
# 
# Where:
# NOPAT = Net Operating Profit After Taxes
#
# Desired Value:
# A higher ROIC value is generally preferable as it signifies that the company is efficiently generating 
# returns from its invested capital. Like other ratios, it's valuable to compare ROIC values of different 
# firms in the same industry.
#
# Note: This script uses hard-coded values for demonstration. For real-world applications, 
# actual financial data values should be input.

def convert_to_actual_value(value_in_millions):
    return value_in_millions * 1000000

# Hard-coded values (in million dollar format for consistency)

nopat_in_millions = 20.00  # Net Operating Profit After Taxes: Example: $20,000,000
invested_capital_in_millions = 120.00  # Example: $120,000,000

# Convert the values
nopat = convert_to_actual_value(nopat_in_millions)
invested_capital = convert_to_actual_value(invested_capital_in_millions)

# Calculate ROIC
roic = nopat / invested_capital

# Output the results
print(f"Return on Invested Capital (ROIC): {roic*100:.2f}%")

if roic > 0.15:  # Assuming 15% as a good benchmark, but this can vary based on industry and other factors.
    print("The company is effectively using its invested capital to generate returns.")
else:
    print("The company might not be efficiently using its invested capital.")