# Function to calculate net income based on revenue, cost of goods sold, operating expenses, and tax rate
def calculate_net_income(revenue, cogs, operating_expenses, tax_rate):
    gross_profit = revenue - cogs
    operating_income = gross_profit - operating_expenses
    net_income_before_tax = operating_income
    net_income = net_income_before_tax * (1 - tax_rate)
    return net_income

# Base-case values in million dollars
base_revenue = 710.72
base_cogs = 40.35
base_operating_expenses = 620.14
base_tax_rate = 0.005  # 0.5%

# Sensitivity values for revenue
sensitivity_values = [-0.10, -0.05, 0, 0.05, 0.10]

print("Sensitivity Analysis on Revenue:")
print("--------------------------------")

for sensitivity in sensitivity_values:
    # Adjust the revenue based on the sensitivity value
    adjusted_revenue = base_revenue * (1 + sensitivity)
    
    # Calculate the net income based on the adjusted revenue
    adjusted_net_income = calculate_net_income(adjusted_revenue, base_cogs, base_operating_expenses, base_tax_rate)
    
    # Output the results
    print(f"When revenue changes by {sensitivity*100:+.2f}%, Net Income = ${adjusted_net_income:.2f} million")
