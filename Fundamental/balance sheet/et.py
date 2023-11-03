# Equity Turnover Calculator
# --------------------------
# Overview:
# The Equity Turnover ratio provides insight into the effectiveness with which a company 
# utilizes its equity to generate revenue. It's an important metric in assessing operational 
# efficiency and investment attractiveness.
#
# Formula:
# Equity Turnover = Net Sales / Average Shareholder's Equity
#
# Desired Value:
# A high equity turnover ratio suggests that a company is effectively using its equity to 
# generate sales. Conversely, a low ratio may indicate inefficiency or over-capitalization.
# It's crucial to compare the ratio with industry benchmarks as standards can vary.
#

# Hard-coded values in millions as decimals (e.g., 1.00 is $1 million)

# Net Sales for the period (in $1M)
net_sales = 749.00  

# Average Shareholder's Equity for the period (in $1M)
# This can be calculated as (Beginning Equity + Ending Equity) / 2
beginning_equity = 6436.00  
ending_equity = 4082.00  
average_equity = (beginning_equity + ending_equity) / 2

# Calculate Equity Turnover for the company
equity_turnover = net_sales / average_equity

# Industry average hard-coded values (in millions as decimals)
industry_avg_net_sales = 700.00  # Example value
industry_avg_beginning_equity = 6000.00  # Example value
industry_avg_ending_equity = 4200.00  # Example value
industry_avg_equity = (industry_avg_beginning_equity + industry_avg_ending_equity) / 2

# Calculate Industry Average Equity Turnover
industry_avg_equity_turnover = industry_avg_net_sales / industry_avg_equity

# Factors and Scenarios that Could Influence Equity Turnover
print("\n--------- Factors and Scenarios Affecting Equity Turnover ---------")
print("1. Company Scale: Larger companies may have lower turnover due to more conservative strategies.")
print("2. Business Model: Asset-light models often have higher turnover.")
print("3. Market Conditions: Cyclical sectors can see fluctuations in turnover.")
print("4. Strategic Changes: Mergers or divestitures can temporarily affect the turnover.")
print("5. Capital Structure: A higher level of debt might dilute the equity base, affecting turnover.")

# Output the results
print(f"\nNet Sales (in $1M): ${net_sales:.2f}M")
print(f"Average Shareholder's Equity (in $1M): ${average_equity:.2f}M")
print(f"Company's Equity Turnover: {equity_turnover:.2f} times")
print(f"Industry Average Equity Turnover: {industry_avg_equity_turnover:.2f} times")

if equity_turnover > industry_avg_equity_turnover:
    print("\nThe company's Equity Turnover is above the industry average. This indicates:")
    print("1. Effective utilization of shareholder equity to generate sales.")
    print("2. The company may be achieving a higher ROI for its shareholders.")
    print("\nIt's beneficial to assess whether this higher turnover is sustainable over the long term.")
  
elif equity_turnover == industry_avg_equity_turnover:
    print("\nThe company's Equity Turnover matches the industry average. This could mean:")
    print("1. The company is operating in line with industry norms.")
    print("2. It neither excels nor lags in using its equity effectively.")
    print("\nIt's worth investigating how peers achieve their turnover rates for comparative analysis.")
  
else:
    print("\nThe company's Equity Turnover is below the industry average. This suggests:")
    print("1. Potential inefficiency or over-capitalization in using equity.")
    print("2. The company may be more risk-averse, holding more equity for stability.")
    print("\nA lower turnover isn't necessarily bad but warrants a deeper analysis of the company's strategy and market position.")
