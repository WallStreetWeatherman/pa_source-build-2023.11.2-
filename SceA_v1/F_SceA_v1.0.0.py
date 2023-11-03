# Scenario Analysis for Revenues

def net_income_scenario(revenue, cost_of_goods_sold, operating_expenses, tax_rate):
    gross_profit = revenue - cost_of_goods_sold
    operating_income = gross_profit - operating_expenses
    taxable_income = operating_income  # Simplifying assumption
    tax = taxable_income * tax_rate
    net_income = taxable_income - tax
    return net_income

# Define the scenarios
scenarios = {
    "worst_case": 113.24,  # revenue in $ million
    "base_case": 710.72,   # revenue in $ million
    "best_case": 1308.20    # revenue in $ million
}

# Other parameters (constant across all scenarios)
cost_of_goods_sold = 40.35  # in $ million
operating_expenses = 620.14  # in $ million
tax_rate = 0.005  # 0.5%

# Perform scenario analysis
scenario_results = {}
for scenario, revenue in scenarios.items():
    net_income = net_income_scenario(revenue, cost_of_goods_sold, operating_expenses, tax_rate)
    scenario_results[scenario] = net_income

# Display the results
print("Scenario Analysis Results:")
for scenario, net_income in scenario_results.items():
    print(f"{scenario.capitalize()}: Net Income = ${net_income} million")
