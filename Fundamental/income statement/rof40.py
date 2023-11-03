# Rule of 40 Calculation for SaaS Companies
# -----------------------------------------
# Overview:
# The Rule of 40 is a heuristic some investors use for software or SaaS-based companies. It states that 
# a healthy SaaS company's growth rate and profit margin should sum to at least 40%. The idea is to balance 
# growth and profitability in high-growth technology sectors, especially SaaS.
#
# Desired Value:
# The combined value of the growth rate and profit margin should be 40% or higher. A combined value 
# below 40% might indicate that the company is neither growing quickly enough nor profitable enough.

# Hardcoded values for the company
revenue_last_year = 85.00 # Revenues in Tikr
revenue_this_year = 100.00
net_income_this_year = 1177.00 # Net Income in Tikr

# Hardcoded values for the industry average
industry_avg_revenue_last_year = 80.00  # Hypothetical average industry revenue from the previous year
industry_avg_revenue_this_year = 96.00  # Hypothetical average industry revenue this year
industry_avg_net_income_this_year = 322.00  # Hypothetical average industry net income this year

# Calculate Growth Rate and Profit Margin
def calculate_growth_rate(last_year, this_year):
    """Calculate annual growth rate."""
    return ((this_year - last_year) / last_year) * 100

def calculate_profit_margin(revenue, net_income):
    """Calculate profit margin as a percentage."""
    return (net_income / revenue) * 100

# Company's calculations
company_growth_rate = calculate_growth_rate(revenue_last_year, revenue_this_year)
company_profit_margin = calculate_profit_margin(revenue_this_year, net_income_this_year)
company_rule_of_40_value = company_growth_rate + company_profit_margin

# Industry's calculations
industry_growth_rate = calculate_growth_rate(industry_avg_revenue_last_year, industry_avg_revenue_this_year)
industry_profit_margin = calculate_profit_margin(industry_avg_revenue_this_year, industry_avg_net_income_this_year)
industry_rule_of_40_value = industry_growth_rate + industry_profit_margin

print(f"Company's Growth Rate: {company_growth_rate:.2f}%")
print(f"Company's Profit Margin: {company_profit_margin:.2f}%")
print(f"Company's Rule of 40 Value: {company_rule_of_40_value:.2f}%")
print(f"\nIndustry Average Growth Rate: {industry_growth_rate:.2f}%")
print(f"Industry Average Profit Margin: {industry_profit_margin:.2f}%")
print(f"Industry Average Rule of 40 Value: {industry_rule_of_40_value:.2f}%")

# Interpretation
if company_rule_of_40_value >= 40.0 and company_rule_of_40_value >= industry_rule_of_40_value:
    print("\nThe company meets or exceeds the Rule of 40 and is also above the industry average, indicating a strong balance of growth and profitability.")
    print("\nFactors possibly contributing to this strong position include:")
    print("- Efficient scaling with controlled expenses, leading to profitable growth.")
    print("- Successful customer retention strategies, reducing churn.")
    print("- Introduction of new features or services that attract customers without significantly raising costs.")
    print("- Operational efficiencies or technological advancements leading to higher profit margins.")
    print("- Strong market positioning or unique value proposition, making it a preferred choice for customers.")
    
elif company_rule_of_40_value >= 40.0:
    print("\nThe company meets or exceeds the Rule of 40, indicating a healthy balance of growth and profitability.")
    print("\nPossible reasons for achieving this balance could be:")
    print("- Consistent revenue streams, possibly through long-term contracts or high recurring revenue.")
    print("- Strategic investments in growth avenues which have begun to yield returns.")
    print("- Efficient cost management and optimization strategies in place.")
    print("- Beneficial external factors, such as favorable industry trends or regulations.")

else:
    print("\nThe company does not meet the Rule of 40, suggesting it might not be growing quickly enough or is not sufficiently profitable.")
    print("\nFactors possibly contributing to this discrepancy include:")
    print("- High customer acquisition costs eating into the profit margins.")
    print("- High upfront investments in infrastructure or R&D which haven't yet provided returns.")
    print("- Facing stiff competition leading to higher marketing spends or discounting.")
    print("- External challenges such as regulatory hurdles, adverse market conditions, or supply chain disruptions.")
    print("- Inefficiencies in operations leading to increased costs.")