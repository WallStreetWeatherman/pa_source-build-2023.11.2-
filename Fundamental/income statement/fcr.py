# Fixed Cost Ratio Calculator
# ---------------------------
# Overview:
# The Fixed Cost Ratio is a measure that indicates the portion of total revenue taken up by fixed costs.
# It provides insights into the company's cost structure and its operational efficiency.
# By understanding the fixed cost ratio, businesses can strategize on how to manage their fixed costs in relation to revenue changes.
#
# Formula:
# Fixed Cost Ratio = Fixed Costs / Total Revenue
#
# Desired Value:
# A lower Fixed Cost Ratio is generally desired as it indicates that a lesser portion of revenue is consumed by fixed costs, allowing for greater operational flexibility.
# A higher ratio may indicate potential challenges during periods of decreased revenue.
#
# Note: This script uses hard-coded values for demonstration. For real-world applications,
# actual fixed costs and total revenue values should be input.

# Hard-coded values in millions as decimals (e.g., 1.00 is $1 million)

# Fixed Costs for the period (in $1M)
fixed_costs = 5.00  # Example value representing $5 million

# Total Revenue for the period (in $1M)
total_revenue = 20.00  # Example value representing $20 million

# Calculate Fixed Cost Ratio
fixed_cost_ratio = fixed_costs / total_revenue

# Output the results
print(f"Fixed Costs (in $1M): ${fixed_costs:.2f}M")
print(f"Total Revenue (in $1M): ${total_revenue:.2f}M")
print(f"Fixed Cost Ratio: {fixed_cost_ratio:.2%}")
print("A lower Fixed Cost Ratio suggests a smaller portion of revenue is consumed by fixed costs, indicating greater operational efficiency.")

