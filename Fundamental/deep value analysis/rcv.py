# Replacement Cost Valuation
# --------------------------
# Overview:
# The Replacement Cost Valuation method values a company based on how much it would cost to replace its assets. 
# This approach can be particularly useful for sectors like utilities or commodities where the physical assets 
# (like plants, infrastructure, etc.) form a significant portion of the company's value.
#
# Desired Value:
# Generally, if the company's market value is substantially higher than its replacement cost, it might be 
# overvalued. Conversely, if the market value is significantly below the replacement cost, the company might be 
# undervalued. However, interpretation should consider other factors like the profitability of assets, growth 
# prospects, and more.

# Hardcoded values (using the format where 1 million is represented as 1.00, 10 million as 10.00, etc.)
current_asset_value = 150.00  # Current value of the company's assets, e.g., $150 million
replacement_costs = {
    "Land": 50.00,  # Cost to acquire similar land
    "Buildings": 40.00,  # Cost to build similar buildings
    "Machinery": 35.00,  # Cost to buy similar machinery
    "Intellectual Property": 15.00,  # Cost to develop/acquire similar intellectual property
    "Other Assets": 10.00  # Cost of other assets
}

def calculate_total_replacement_cost(replacement_costs):
    """Calculate the total replacement cost of the company's assets."""
    return sum(replacement_costs.values())

total_replacement_cost = calculate_total_replacement_cost(replacement_costs)

print("Breakdown of Replacement Costs (in $ million):")
for asset, cost in replacement_costs.items():
    print(f"{asset}: ${cost:.2f}")

print(f"\nTotal Replacement Cost: ${total_replacement_cost:.2f} million")
print(f"Current Asset Value: ${current_asset_value:.2f} million")

# Interpretation
if current_asset_value > total_replacement_cost:
    print("\nThe company may be overvalued based on replacement costs.")
elif current_asset_value == total_replacement_cost:
    print("\nThe company might be fairly valued based on replacement costs.")
else:
    print("\nThe company may be undervalued based on replacement costs. However, always consider other factors like the profitability of assets, growth prospects, etc.")
