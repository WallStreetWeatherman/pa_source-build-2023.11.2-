# Book Value Calculation with Industry Average
# -------------------------------------------
# Overview:
# Book Value is calculated as the difference between a company's Total Assets and Total Liabilities.
# It represents the net asset value of the company that belongs to the shareholders.
#
# Desired Value:
# A higher Book Value is generally considered favorable as it indicates more assets relative to liabilities.
# A lower Book Value may suggest financial weakness.
# Comparing the company's Book Value with the industry average can provide insights into the company's financial health relative to its peers.

def convert_to_actual_value(value):
    """Converts the value in the format of 1.00 to actual $1 million."""
    return value * 1000000

# Hardcoded values (in $ millions, represented as 1.00 for 1 million)
total_assets = 16304.00  # Example: $16.3 billion
total_liabilities = 12094.00  # Example: $12.1 billion

# Hardcoded values for industry average (in $ millions, represented as 1.00 for 1 million)
industry_avg_assets = 15000.00  # Example: $15 billion
industry_avg_liabilities = 11000.00  # Example: $11 billion

# Calculate Book Value
book_value = convert_to_actual_value(total_assets) - convert_to_actual_value(total_liabilities)
industry_avg_book_value = convert_to_actual_value(industry_avg_assets) - convert_to_actual_value(industry_avg_liabilities)

# Output the result
print("Book Value Calculation:\n")
print("Calculated Book Value for the Company: ${:,.2f}".format(book_value))
print("Industry Average Book Value: ${:,.2f}".format(industry_avg_book_value))

# Compare the company's book value with the industry average
if book_value > industry_avg_book_value:
    print("The company's Book Value is higher than the industry average, indicating a strong financial position relative to its peers.")
    print("Factors and Scenarios Affecting the Ratio:")
    print("1. Asset Accumulation: The company may have accumulated a large asset base, contributing to a higher book value.")
    print("2. Low Leverage: A lower debt burden relative to peers suggests more robust financial health.")
    print("3. Operational Efficiency: High profitability can contribute to a stronger asset base.")
elif book_value == industry_avg_book_value:
    print("The company's Book Value is in line with the industry average.")
    print("Factors and Scenarios Affecting the Ratio:")
    print("1. Balanced Operations: The company seems to be operating on industry norms, neither accumulating excessive assets nor liabilities.")
    print("2. Steady State: The company may not be in a phase of rapid expansion or contraction.")
else:
    print("The company's Book Value is lower than the industry average, suggesting potential financial weakness relative to its peers.")
    print("Factors and Scenarios Affecting the Ratio:")
    print("1. High Debt: The company might be more leveraged than its peers, affecting its book value negatively.")
    print("2. Asset Depreciation: An aging asset base could contribute to a lower book value.")
    print("3. Recent Losses: Operational inefficiencies or other adverse conditions could have led to a depletion of assets.")
    