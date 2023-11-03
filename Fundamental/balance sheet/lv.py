# Liquidation Value Calculation
# -----------------------------
# Overview:
# The Liquidation Value provides an estimation of the value of a company's tangible assets if they were to 
# be quickly sold off (or "liquidated"). It is a conservative valuation metric because it doesn't account 
# for intangible assets or future profitability, just the net current value of physical assets after liabilities.
#
# Desired Value:
# Generally, a higher liquidation value indicates more underlying value in the company's tangible assets. 
# If the liquidation value is significantly lower than the company's market cap, it could indicate the stock 
# is overvalued or that a significant portion of the company's value is based on intangible assets or future expectations.

# Hardcoded values for the company
current_assets = 100.00  # Company's total current assets (e.g., $100 million)
property_plant_equipment = 50.00  # Company's property, plant, and equipment value (e.g., $50 million)
total_liabilities = 90.00  # Company's total liabilities (e.g., $90 million)

# Hardcoded values for the industry average
industry_avg_current_assets = 110.00
industry_avg_property_plant_equipment = 55.00
industry_avg_total_liabilities = 95.00

def calculate_liquidation_value(current_assets, pp_e, total_liabilities):
    """Calculate liquidation value."""
    return current_assets + pp_e - total_liabilities

# Calculate for the company
liquidation_value = calculate_liquidation_value(current_assets, property_plant_equipment, total_liabilities)

# Calculate for the industry average
industry_liquidation_value = calculate_liquidation_value(industry_avg_current_assets, industry_avg_property_plant_equipment, industry_avg_total_liabilities)

# Output the results
print(f"Company's Liquidation Value: ${liquidation_value:.2f} million")
print(f"Industry Average Liquidation Value: ${industry_liquidation_value:.2f} million")

# Interpretation and Discussing Influencing Factors
if liquidation_value > industry_liquidation_value:
    print(f"\nThe company's liquidation value is above the industry average, indicating a relatively strong position in tangible assets. Factors that may influence this include:")
    print("- A lower debt-to-asset ratio, implying fewer liabilities relative to assets.")
    print("- A well-maintained portfolio of property, plant, and equipment.")
    print("- Effective working capital management, leading to higher current assets.")
else:
    print(f"\nThe company's liquidation value is below the industry average, suggesting caution for investors emphasizing tangible asset backing. Factors that may contribute to this include:")
    print("- High short-term or long-term debt, affecting the liabilities.")
    print("- Depreciated or outdated physical assets.")
    print("- Inadequate inventory management, tying up cash in unsold goods.")
    