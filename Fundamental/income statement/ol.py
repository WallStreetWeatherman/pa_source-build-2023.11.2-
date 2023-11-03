# Operating Leverage Calculator
# ------------------------------
# Overview:
# Operating leverage measures the proportion of fixed costs in the total cost structure. 
# High operating leverage means the company has a significant portion of fixed costs, 
# indicating that a percentage increase in revenue will result in a larger percentage increase in operating income.
#
# Formula:
# Degree of Operating Leverage (DOL) = Contribution Margin / Operating Income
# Contribution Margin = Sales - Variable Costs
# Operating Income = Contribution Margin - Fixed Costs
#
# Desired Value:
# High operating leverage can be both beneficial and risky. While it means that a revenue increase 
# will significantly boost operating income, a decrease in revenue might amplify the drop in income.
#
# Note: This script uses hard-coded values for demonstration. For real-world applications,
# sales, variable costs, and fixed costs values should be input.

# Hard-coded values in millions as decimals (e.g., 1.00 is $1 million)

# Sales for the period (in $1M)
sales = 20.00  # Example value representing $20 million

# Variable Costs for the period (in $1M)
variable_costs = 8.00  # Example value representing $8 million

# Fixed Costs for the period (in $1M)
fixed_costs = 5.00  # Example value representing $5 million

# Calculate Contribution Margin
contribution_margin = sales - variable_costs

# Calculate Operating Income
operating_income = contribution_margin - fixed_costs

# Calculate Degree of Operating Leverage
DOL = contribution_margin / operating_income

# Output the results
print(f"Contribution Margin (in $1M): ${contribution_margin:.2f}M")
print(f"Operating Income (in $1M): ${operating_income:.2f}M")
print(f"Degree of Operating Leverage: {DOL:.2f}")
print("A high DOL indicates that a significant change in sales will result in a larger change in operating income.")

