# Relative Value Methods
# ----------------------
# Overview:
# The relative value method compares the company to other firms in the same industry or sector.
# Metrics like the Price-to-Sales (P/S) and Price-to-Free-Cash-Flow (P/FCF) ratios are used, 
# especially when earnings might not be a reliable indicator of value.
#
# Desired Value:
# A lower P/S or P/FCF ratio can indicate potential undervaluation compared to peers.
# However, industry and sector averages should be considered for a comprehensive analysis.

# Hardcoded values for the company
company_sales = 24442.00 # Revenues in Tikr
company_free_cash_flow = 162.00 # Unlevered Free Cash Flow in Tikr Screener
company_market_cap = 3029.00 # Market Cap in Tikr

# Hardcoded values for industry average (hypothetical values for this example)
industry_avg_sales = 4840.00  
industry_avg_free_cash_flow = 442.00  
industry_avg_market_cap = 44750.00  

# Calculate Price-to-Sales (P/S) ratio
def calculate_ps_ratio(market_cap, sales):
    """Calculate P/S ratio."""
    return market_cap / sales

# Calculate Price-to-Free-Cash-Flow (P/FCF) ratio
def calculate_pfcf_ratio(market_cap, free_cash_flow):
    """Calculate P/FCF ratio."""
    return market_cap / free_cash_flow

# Company's calculations
company_ps_ratio = calculate_ps_ratio(company_market_cap, company_sales)
company_pfcf_ratio = calculate_pfcf_ratio(company_market_cap, company_free_cash_flow)

# Industry's calculations
industry_avg_ps_ratio = calculate_ps_ratio(industry_avg_market_cap, industry_avg_sales)
industry_avg_pfcf_ratio = calculate_pfcf_ratio(industry_avg_market_cap, industry_avg_free_cash_flow)

# ... [code remains unchanged up until the print statements]

print(f"Company's Price-to-Sales (P/S) Ratio: {company_ps_ratio:.2f}")
print(f"Company's Price-to-Free-Cash-Flow (P/FCF) Ratio: {company_pfcf_ratio:.2f}")
print(f"\nIndustry Average Price-to-Sales (P/S) Ratio: {industry_avg_ps_ratio:.2f}")
print(f"Industry Average Price-to-Free-Cash-Flow (P/FCF) Ratio: {industry_avg_pfcf_ratio:.2f}")

print("\nFactors and Scenarios influencing the ratios:")
print("- **Profitability Margins:** Companies with higher profit margins might justify higher P/S ratios.")
print("- **Growth Prospects:** Firms expected to grow faster than their peers might also trade at higher multiples.")
print("- **Business Model:** Recurring revenue models, such as subscription-based services, can command higher P/S ratios.")
print("- **Capital Expenditure Needs:** Companies that can generate high free cash flow with less reinvestment (lower CapEx) might have more favorable P/FCF ratios.")
print("- **Competitive Position:** Firms with strong competitive moats may trade at premium valuations.")
print("- **Industry Cyclicality:** During industry upturns, companies might be valued higher based on near-term sales and cash flow boosts.")
print("- **Economic Conditions:** During expansive economic phases, investors might be willing to pay more for sales and cash flows.")
print("- **Debt Levels:** Higher debt can suppress P/FCF if interest costs reduce the available free cash flow.")

print("\nInterpretation:")
if company_ps_ratio < industry_avg_ps_ratio:
    print("Based on the P/S ratio, the company might be undervalued compared to industry peers. However, consider the firm's profitability, growth prospects, and business model.")
else:
    print("From the P/S perspective, the company appears fairly valued or overvalued compared to the industry. Scrutinize factors like its growth potential and competitive position.")

if company_pfcf_ratio < industry_avg_pfcf_ratio:
    print("Using the P/FCF ratio as a lens, the company seems undervalued against the industry average. But, gauge its CapEx needs and debt situation.")
else:
    print("From a P/FCF standpoint, the company seems fairly valued or overvalued relative to industry peers. Delve into aspects such as its cash flow stability and capital expenditure trends.")
