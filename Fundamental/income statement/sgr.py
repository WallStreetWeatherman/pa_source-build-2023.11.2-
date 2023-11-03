# Sustainable Growth Rate (SGR) Calculator
# ----------------------------------------
# Overview:
# The Sustainable Growth Rate (SGR) projects the growth rate a company can expect and sustain 
# by using its earnings, without the need for external equity financing. It's a crucial metric 
# for businesses looking to expand without diluting ownership.
#
# Formula:
# SGR = Return on Equity (ROE) * Retention Ratio
# Where,
# Retention Ratio = 1 - Dividend Payout Ratio
# Dividend Payout Ratio = Dividends / Net Income
#
# Desired Value:
# A higher SGR indicates a company's potential to grow using its own financial resources.
# However, maintaining a balance between high growth and financial stability is essential.
#

# Company's data:
net_income_company = 1177.00 # Net Income in Tikr
dividends_company = 173.00  # Common Dividends Paid in Tikr // Always make Positive Num.
equity_company = 4082.00 # Total Equity in Tikr

# Industry average data:
net_income_industry = 322.00
dividends_industry = 16.00
equity_industry = 4220.00

# Company's calculations
roe_company = net_income_company / equity_company
dividend_payout_ratio_company = dividends_company / net_income_company
retention_ratio_company = 1 - dividend_payout_ratio_company
sgr_company = roe_company * retention_ratio_company

# Industry average calculations
roe_industry = net_income_industry / equity_industry
dividend_payout_ratio_industry = dividends_industry / net_income_industry
retention_ratio_industry = 1 - dividend_payout_ratio_industry
sgr_industry = roe_industry * retention_ratio_industry

# Display results
print(f"Company's Net Income (in $1M): ${net_income_company:.2f}M")
print(f"Company's Dividends Paid (in $1M): ${dividends_company:.2f}M")
print(f"Company's Shareholder's Equity (in $1M): ${equity_company:.2f}M")
print(f"Company's Sustainable Growth Rate (SGR): {sgr_company:.2%}\n")

print(f"Industry Average Net Income (in $1M): ${net_income_industry:.2f}M")
print(f"Industry Average Dividends Paid (in $1M): ${dividends_industry:.2f}M")
print(f"Industry Average Shareholder's Equity (in $1M): ${equity_industry:.2f}M")
print(f"Industry Average Sustainable Growth Rate (SGR): {sgr_industry:.2%}\n")

if sgr_company > sgr_industry:
    print("The company's SGR is above the industry average, indicating potential for higher growth using its own resources.")
    print("\nFactors influencing a higher SGR may include:")
    print("- Effective capital allocation decisions.")
    print("- Efficient operational processes leading to higher profitability.")
    print("- A competitive advantage in the industry, leading to higher net income.")
    print("- A company policy to reinvest a significant portion of its earnings, as evidenced by a low dividend payout.")
    
elif sgr_company < sgr_industry:
    print("The company's SGR is below the industry average, suggesting potential challenges in growing without external financing.")
    print("\nFactors potentially contributing to a lower SGR include:")
    print("- Larger proportion of earnings being distributed as dividends, leaving less for reinvestment.")
    print("- Challenges in maintaining profitability and maximizing shareholder equity.")
    print("- External challenges, like market saturation or strong competition.")
    print("- Operational inefficiencies leading to reduced net income.")
    
else:
    print("The company's SGR aligns with the industry average.")
    print("\nBeing in line with industry averages suggests the company is performing on par with peers. Continued monitoring is essential to ensure that the company adapts to changing industry dynamics.")
    