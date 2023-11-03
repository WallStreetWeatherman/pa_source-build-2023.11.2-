# PEGY Ratio Calculation
# ----------------------
# Overview:
# The PEGY (Price/Earnings to Growth and Dividend Yield) Ratio is an extension of the PEG ratio. 
# It takes into account both the projected earnings growth and the dividend yield of a company. 
# It is useful for valuing companies that return significant capital to shareholders through dividends.
#
# Desired Value:
# A lower PEGY ratio typically indicates an undervalued company, or less pay for each unit of earnings growth 
# and dividend yield. However, interpretation might vary depending on industry and other factors.

# Hardcoded values for the company
company_price_per_share = 50.00
company_earnings_per_share = 5.00
company_projected_growth = 0.10
company_dividend_yield = 0.04

# Hardcoded values for the industry average
industry_avg_price_per_share = 52.00
industry_avg_earnings_per_share = 5.20
industry_avg_projected_growth = 0.11
industry_avg_dividend_yield = 0.03

def calculate_pegy_ratio(price_per_share, earnings_per_share, projected_growth, dividend_yield):
    """Calculate the PEGY Ratio."""
    pe_ratio = price_per_share / earnings_per_share
    return pe_ratio / (projected_growth + dividend_yield)

company_pegy_ratio = calculate_pegy_ratio(company_price_per_share, company_earnings_per_share, company_projected_growth, company_dividend_yield)
industry_avg_pegy_ratio = calculate_pegy_ratio(industry_avg_price_per_share, industry_avg_earnings_per_share, industry_avg_projected_growth, industry_avg_dividend_yield)

print(f"Company's PEGY Ratio: {company_pegy_ratio:.2f}")
print(f"Industry Average PEGY Ratio: {industry_avg_pegy_ratio:.2f}")

# Output and Interpretation
print("PEGY Ratio Analysis:\n")
print(f"Company's PEGY Ratio: {company_pegy_ratio:.2f}")
print(f"Industry Average PEGY Ratio: {industry_avg_pegy_ratio:.2f}")

if company_pegy_ratio < industry_avg_pegy_ratio:
    print("The company's stock appears undervalued relative to the industry average. Influencing factors could include:")
    print("- Stronger projected earnings growth.")
    print("- Higher dividend yield, offering income potential.")
    print("- Greater operational efficiency leading to better margins.")
    print("- Potential for share price appreciation, creating a favorable investment scenario.")
elif company_pegy_ratio == industry_avg_pegy_ratio:
    print("The company's stock seems fairly priced compared to the industry average. This could be due to:")
    print("- Comparable earnings growth and dividend yield to industry peers.")
    print("- Balanced risk-reward profile.")
    print("- Market already pricing in future growth and dividend prospects.")
else:
    print("The company's stock appears overvalued relative to the industry average. Reasons for this might be:")
    print("- Lower projected earnings growth compared to peers.")
    print("- Lower dividend yield, reducing the income component of the stock.")
    print("- Potential headwinds such as increasing competition, regulatory challenges, or rising costs.")
    print("- Investor over-optimism or market speculation driving up the share price.")