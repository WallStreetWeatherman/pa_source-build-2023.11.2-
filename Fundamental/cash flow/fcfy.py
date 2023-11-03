# FCF Yield Calculation
# ---------------------
# Overview:
# The FCF Yield measures the firm's ability to generate cash relative to its size.
# It is calculated by dividing the company's Free Cash Flow by its Market Capitalization.
#
# Desired Value:
# A higher FCF Yield indicates that the company is generating more cash in relation to its size.
# This could be seen as an indicator that the company might be undervalued.

# Hardcoded values for the company (in the format where 1 million is represented as 1.00, etc.)
company_free_cash_flow = 5.00  # Company's Free Cash Flow (e.g., $5 million)
company_market_cap = 100.00    # Company's Market Capitalization (e.g., $100 million)

# Hardcoded industry average values
industry_average_free_cash_flow = 60.00  # Industry's Average Free Cash Flow (e.g., $60 million)
industry_average_market_cap = 1200.00  # Industry's Average Market Capitalization (e.g., $1200 million)

# Calculate FCF Yield
def calculate_fcf_yield(free_cash_flow, market_cap):
    """Calculate the Free Cash Flow Yield based on the free cash flow and market cap."""
    return free_cash_flow / market_cap

company_fcf_yield = calculate_fcf_yield(company_free_cash_flow, company_market_cap)
industry_fcf_yield = calculate_fcf_yield(industry_average_free_cash_flow, industry_average_market_cap)

print(f"Company's Free Cash Flow (FCF) Yield: {company_fcf_yield:.2f} or {company_fcf_yield*100:.2f}%")
print(f"Industry Average FCF Yield: {industry_fcf_yield:.2f} or {industry_fcf_yield*100:.2f}%")

print(f"Company's Free Cash Flow (FCF) Yield: {company_fcf_yield:.2f} or {company_fcf_yield*100:.2f}%")
print(f"Industry Average FCF Yield: {industry_fcf_yield:.2f} or {industry_fcf_yield*100:.2f}%\n")

# Interpretation
if company_fcf_yield > industry_fcf_yield:
    print("The company's FCF Yield is above the industry average, suggesting it might be undervalued relative to its peers. Factors contributing to this could include:")
    print("- Stronger operational efficiency leading to higher free cash flow generation.")
    print("- The market might not have fully recognized the company's potential or recent positive developments, leading to a lower market capitalization.")
    print("- Strategic decisions that enhanced cash flow generation, such as cost-cutting, efficient capital allocation, or lucrative business ventures.")
    print("- Potential external factors such as favorable economic conditions, beneficial regulations, or industry tailwinds benefiting the company.")
    
elif company_fcf_yield == industry_fcf_yield:
    print("The company's FCF Yield is in line with the industry average. This suggests:")
    print("- The company operates at a similar efficiency level to its peers in terms of cash flow generation.")
    print("- The market perception of the company's valuation is aligned with industry norms.")
    print("- Potential headwinds or tailwinds affecting the industry are likely impacting the company in a similar manner as its peers.")
    
else:
    print("The company's FCF Yield is below the industry average, indicating it might be overvalued compared to its peers. Possible scenarios and factors include:")
    print("- The company might have faced recent challenges leading to decreased free cash flow.")
    print("- Over-optimistic market sentiment might be driving the company's market capitalization higher without a corresponding increase in FCF.")
    print("- Significant recent capital expenditures or other cash outflows affecting free cash flow generation.")
    print("- External challenges such as tough economic conditions, regulatory hurdles, or industry headwinds might be impacting the company more than its peers.")
    