# Gross Profit Margin Calculation
# -------------------------------
# Overview:
# The Gross Profit Margin ratio measures the percentage of revenue that exceeds the cost of goods sold.
# It helps in understanding how efficiently a company produces goods.
#
# Desired Value:
# A higher Gross Profit Margin indicates that the company retains more money on each dollar of sales to 
# cover its other costs. However, interpretation may differ based on industry standards.

# Hardcoded values for the company (in the format where 1 million is represented as 1.00, etc.)
company_revenue = 100.00         # Company's revenue (e.g., $100 million)
company_cogs = 65.00             # Company's cost associated with producing goods (e.g., $65 million)

# Hardcoded values for the industry average
industry_revenue = 1000.00       # Industry's average revenue (e.g., $1000 million)
industry_cogs = 700.00           # Industry's average cost associated with producing goods (e.g., $700 million)

# Calculate Gross Profit Margin
def calculate_gross_profit_margin(revenue, cogs):
    """Calculate Gross Profit Margin as a percentage."""
    gross_profit = revenue - cogs
    return (gross_profit / revenue) * 100

company_gross_profit_margin = calculate_gross_profit_margin(company_revenue, company_cogs)
industry_avg_gpm = calculate_gross_profit_margin(industry_revenue, industry_cogs)

print(f"Company's Gross Profit Margin: {company_gross_profit_margin:.2f}%")
print(f"Industry Average Gross Profit Margin: {industry_avg_gpm:.2f}%")

# Interpretation
if company_gross_profit_margin > industry_avg_gpm:
    print("The company's Gross Profit Margin is above the industry average, indicating efficient production.")
    print("\nPossible reasons for a superior Gross Profit Margin include:")
    print("- Effective cost management and sourcing strategies.")
    print("- Ability to command higher prices due to strong brand or unique products.")
    print("- Advanced production technologies leading to cost savings.")
    print("- Reduction in waste or spoilage during production.")
elif company_gross_profit_margin == industry_avg_gpm:
    print("The company's Gross Profit Margin aligns with the industry average. This indicates that the company is performing on par with its competitors in terms of production efficiency.")
else:
    print("The company's Gross Profit Margin is below the industry average. It might be worthwhile to investigate production inefficiencies.")
    print("\nFactors potentially impacting a lower Gross Profit Margin might be:")
    print("- Increased raw material prices without the ability to raise product prices.")
    print("- Outdated production methodologies leading to inefficiencies.")
    print("- Increased competition forcing the company to provide discounts or promotions.")
    print("- Challenges with supply chain leading to higher procurement costs.")