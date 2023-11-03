# Price to Free Cash Flow (P/FCF) Ratio
# -------------------------------------
# Overview:
# The P/FCF ratio is similar to the P/E ratio, but it uses Free Cash Flow instead of earnings. 
# This ratio measures the price investors are willing to pay for each dollar of free cash flow. 
# Free Cash Flow represents the cash that a company can generate after required investments 
# to maintain or expand its asset base. It's considered a reliable measure as it's harder 
# to manipulate compared to earnings.
#
# Desired Value:
# A lower P/FCF suggests that a company might be undervalued relative to its free cash flow 
# generation ability, while a higher P/FCF might indicate potential overvaluation. 
# However, the "good" or "bad" value can vary by industry and the overall market conditions.

# Hardcoded values for the company
company_market_cap = 3029.00 # Market Cap in Tikr
company_annual_free_cash_flow = 162.00 # Unlevered Free Cash Flow in Tikr Screener

# Hardcoded values for the industry average
industry_avg_market_cap = 44750.00  
industry_avg_free_cash_flow = 442.00  

def calculate_pfcf_ratio(market_cap, free_cash_flow):
    """Calculate the Price to Free Cash Flow ratio."""
    if free_cash_flow == 0:
        raise ValueError("Free cash flow should not be zero to calculate the P/FCF ratio.")
    return market_cap / free_cash_flow

company_pfcf_ratio = calculate_pfcf_ratio(company_market_cap, company_annual_free_cash_flow)
industry_avg_pfcf_ratio = calculate_pfcf_ratio(industry_avg_market_cap, industry_avg_free_cash_flow)

print(f"Company's P/FCF Ratio: {company_pfcf_ratio:.2f}")
print(f"Industry Average P/FCF Ratio: {industry_avg_pfcf_ratio:.2f}")

print("\nFactors and Scenarios potentially influencing the P/FCF ratio:")
print("- Cash Flow Consistency: A company with stable and predictable free cash flow might command a higher P/FCF ratio, as investors could see it as less risky.")
print("- Growth Prospects: Companies expected to significantly grow their free cash flow in the future might have higher P/FCF ratios. Investors are willing to pay more today for anticipated future growth.")
print("- Capital Expenditures: High capital expenditures can reduce free cash flow. If the company is heavily investing in its business, it could temporarily depress the P/FCF ratio.")
print("- Debt Levels: High levels of debt can impact a company's ability to generate free cash flow, as more cash might be directed towards debt service. This can influence the P/FCF ratio.")
print("- Industry Dynamics: Some industries naturally have higher P/FCF ratios due to their business models or industry life cycle stage. For instance, tech companies might have higher ratios compared to traditional manufacturing firms.")
print("- Macroeconomic Factors: Economic downturns or uncertain environments can lead investors to prioritize companies with strong cash flow generation, potentially leading to higher P/FCF ratios for those firms.")
print("- Accounting Practices: As the P/FCF ratio uses cash flow, which is less prone to manipulation than earnings, it's considered more reliable. However, differences in accounting practices can still influence the reported free cash flow figures.")

print("\nImplications:")
if company_pfcf_ratio < industry_avg_pfcf_ratio:
    print("The company may be undervalued compared to the industry average based on its P/FCF ratio. This could present a potential investment opportunity, but further analysis is recommended.")
elif company_pfcf_ratio == industry_avg_pfcf_ratio:
    print("The company's valuation appears to be in line with the industry average based on its P/FCF ratio. It's operating at par with its peers in terms of cash flow valuation.")
else:
    print("The company may be overvalued compared to the industry average based on its P/FCF ratio. Investors should exercise caution and investigate the reasons for the high ratio.")
