# Return on Capital Employed (ROCE) Calculator
# --------------------------------------------
# Overview:
# Return on Capital Employed (ROCE) is a financial metric that measures a company's profitability and 
# the efficiency with which its capital is used. In other words, the ratio indicates how well a company 
# is generating profits from its capital. 
#
# Formula:
# ROCE = EBIT / (Total Assets - Current Liabilities)
# 
# Where:
# EBIT = Earnings Before Interest and Taxes
#
# Desired Value:
# A higher ROCE is typically preferable as it indicates that the company is efficient in generating returns
# from its capital. However, it's essential to compare this with ROCE values of other firms in the same industry 
# or sector for a meaningful analysis.
#
# Note: This script uses hard-coded values for demonstration. For real-world applications, 
# actual financial data values should be input.

def convert_to_actual_value(value_in_millions):
    return value_in_millions * 1000000

# Hard-coded values (in million dollar format for consistency)

ebit_in_millions = 15.00  # Earnings Before Interest and Taxes: Example: $15,000,000
total_assets_in_millions = 150.00  # Example: $150,000,000
current_liabilities_in_millions = 30.00  # Example: $30,000,000

# Convert the values
ebit = convert_to_actual_value(ebit_in_millions)
total_assets = convert_to_actual_value(total_assets_in_millions)
current_liabilities = convert_to_actual_value(current_liabilities_in_millions)

# Calculate ROCE
capital_employed = total_assets - current_liabilities
roce = ebit / capital_employed

# Output the results
print(f"Return on Capital Employed (ROCE): {roce*100:.2f}%")

if roce > 0.15:  # Assuming 15% as a good benchmark, but this can vary based on industry and other factors.
    print("The company has a good return on its capital employed.")
else:
    print("The company might not be efficiently using its capital.")
