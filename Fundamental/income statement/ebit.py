# EBIT (Earnings Before Interest and Taxes) Calculation
# -----------------------------------------------------
# Overview:
# EBIT represents a company's operating profit, disregarding the effects of 
# interest and income tax expenses. It's used to analyze the performance 
# of a company's core operations without the influence of capital structure and tax strategy.
#
# Desired Value:
# A higher EBIT indicates that a company is generating more profits from its operations.
# However, it's crucial to compare EBIT values within the same industry or sector to get 
# a more accurate picture of a company's performance.
#
# Note: This script uses hard-coded values. For real-world application, data should be adjusted accordingly.

def convert_to_actual_value(value):
    """Converts the value in the format of 1.00 to actual $1 million."""
    return value * 1000000

# Hard-coded values
revenues = convert_to_actual_value(23606.00)    # Example: $150 million
cost_of_goods_sold = convert_to_actual_value(14818.00)   
operating_expenses = convert_to_actual_value(8337.00)  

# Calculate EBIT
ebit = revenues - cost_of_goods_sold - operating_expenses

# Output the result
print("EBIT (Earnings Before Interest and Taxes) Calculation:\n")
print(f"EBIT: ${ebit/1000000:,.2f} million")

# EBIT Analysis based on its value
if ebit > 0:
    print("The company has a positive EBIT, which suggests strong core operational performance.")
    print("Factors contributing might include:")
    print("- Efficient operational strategies.")
    print("- Successful cost management.")
    print("- High demand for the company's products or services.")
else:
    print("The company has a negative EBIT, indicating challenges in core operational performance.")
    print("Factors contributing might include:")
    print("- Increased competition leading to reduced prices.")
    print("- Higher raw material costs or other direct costs.")
    print("- Inefficient management or operational strategies.")
    print("- Unexpected external events (e.g., supply chain disruptions, regulatory changes).")
    