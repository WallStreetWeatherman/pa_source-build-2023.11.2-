# EV to Sales Calculator
# ----------------------
# Overview:
# EV to Sales (Enterprise Value to Sales) ratio compares the total enterprise value 
# of a company to its sales. This ratio is often used to assess companies in sectors 
# where profitability might not yet be achieved, but significant revenues are being generated.
#
# Formula:
# EV to Sales = Enterprise Value / Sales
#
# Desired Value:
# A lower EV to Sales ratio may indicate that a company is undervalued. 
# However, context is essential, as the acceptable ratio can vary significantly across industries.
#
# Note: This script uses hard-coded values for demonstration. For real-world applications,
# actual company data should be input.

# Hard-coded values in millions as decimals (e.g., 1.00 is $1 million)
# Company-specific values
market_cap = 3176.00  # Market Capitalization
debt = 5972.00  # Total Debt
cash_and_equivalents = 438.00  # Cash and Cash Equivalents
sales = 23606.00  # Total Sales or Revenue for the period

# Industry average values
industry_avg_market_cap = 3500.00  # Example value for industry average market capitalization
industry_avg_debt = 6100.00  # Example value for industry average total debt
industry_avg_cash = 500.00  # Example value for industry average cash and cash equivalents
industry_avg_sales = 24500.00  # Example value for industry average sales

# Calculate Enterprise Value (EV) for the company and industry
company_enterprise_value = market_cap + debt - cash_and_equivalents
industry_enterprise_value = industry_avg_market_cap + industry_avg_debt - industry_avg_cash

# Calculate EV to Sales ratio for the company and industry
company_ev_to_sales = company_enterprise_value / sales
industry_ev_to_sales = industry_enterprise_value / industry_avg_sales

# Factors Influencing EV to Sales
print("\n--------- Factors That Could Influence EV to Sales ---------")
print("1. Market Sentiment: High investor demand can elevate the market cap, and hence EV.")
print("2. Debt Levels: High levels of debt increase enterprise value but can also pose risks.")
print("3. Sales Growth: Rapidly growing sales can justify a higher EV to Sales ratio.")
print("4. Competitive Position: A leading market position might result in a higher EV to Sales.")
print("5. Maturity: Newer companies may have high sales but are not yet profitable, affecting the ratio.")
print("6. Economic Factors: Economic booms or busts can significantly impact sales figures.")

# Output the results
print(f"\nEV to Sales Ratio for the Company: {company_ev_to_sales:.2f}")
print(f"Industry Average EV to Sales Ratio: {industry_ev_to_sales:.2f}")

if company_ev_to_sales < industry_ev_to_sales:
    print("\nThe company's EV to Sales ratio is below the industry average, suggesting it might be undervalued. Consider the following:")
    print("1. Is the company really undervalued, or are there underlying issues depressing the value?")
    print("2. Is the company's sales growth and market position strong enough to warrant investment?")

elif company_ev_to_sales > industry_ev_to_sales:
    print("\nThe company's EV to Sales ratio is above the industry average, indicating it might be overvalued. Think about these aspects:")
    print("1. Is the company actually overvalued, or does it have unique assets or capabilities justifying the higher ratio?")
    print("2. How does the company's debt and profitability compare with its peers?")

else:
    print("\nThe company's EV to Sales ratio aligns with the industry average. Keep these factors in mind:")
    print("1. How is the company performing in terms of profitability and growth?")
    print("2. What is the economic environment and how might it impact future sales?")