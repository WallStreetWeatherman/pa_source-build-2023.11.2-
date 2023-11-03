# Investing to Financing Cash Flow Ratio Calculator
# -------------------------------------------------
# Overview:
# The Investing to Financing Cash Flow Ratio assesses the relationship between cash used for 
# investing activities and the cash generated from financing activities. It can help determine 
# the reliance of a company on external financing compared to its investment activities.
#
# Formula:
# Investing to Financing Cash Flow Ratio = Cash Used for Investing Activities / Cash Generated from Financing Activities
#
# Desired Value:
# A ratio greater than 1 indicates that the company is using more cash for investments 
# than it's raising from financing. A ratio less than 1 suggests that the company is more reliant 
# on external financing than it is on investments. Depending on the company's strategy and life cycle stage, 
# either scenario can be suitable.

def convert_to_actual_value(value_in_millions):
    """Converts the value in the format of 1.00 to actual $1 million."""
    return value_in_millions * 1000000

# Hard-coded values for the company

# Cash Used for Investing Activities
company_investing_cash_flow = convert_to_actual_value(-1169.00) # Cash from Investing in Tikr
# Cash Generated from Financing Activities
company_financing_cash_flow = convert_to_actual_value(-1296.00) # Cash from Financing in Tikr
# Calculate the company's Investing to Financing Cash Flow Ratio
company_ratio = company_investing_cash_flow / company_financing_cash_flow

# Hard-coded values for the industry average

# Industry average cash used for investing activities
industry_investing_cash_flow = convert_to_actual_value(-540.00)  # Placeholder value
# Industry average cash generated from financing activities
industry_financing_cash_flow = convert_to_actual_value(-312.00)  # Placeholder value
# Calculate the industry average Investing to Financing Cash Flow Ratio
industry_ratio = industry_investing_cash_flow / industry_financing_cash_flow

# Output the results
print("Investing to Financing Cash Flow Analysis:\n")
print(f"Company's Calculated Ratio: {company_ratio:.2f}")
print(f"Industry Average Ratio: {industry_ratio:.2f}\n")

# Interpretation
if company_ratio > industry_ratio:
    print("The company's ratio is above the industry average, indicating it uses more cash for investments compared to financing relative to its peers. Possible factors influencing this scenario could be:")
    print("- The company has healthy internal cash reserves or operational cash flow that allows for more investments without relying on external financing.")
    print("- A strategic decision to invest heavily in assets, research & development, or acquisitions to potentially drive future growth.")
    print("- The company might be in a growth phase where it is channeling its resources towards expansion.")
    print("- A favorable financial market condition that allows the company to secure investments at lower costs.")
    
elif company_ratio == industry_ratio:
    print("The company's ratio is on par with the industry average. This suggests:")
    print("- The company's reliance on external financing and its investment strategies align with the industry standards.")
    print("- It may be operating in a stable phase, with financial activities reflecting the industry norms.")
    print("- The industry as a whole might be following a certain trend or responding to macroeconomic factors in a uniform way.")
    
else:
    print("The company's ratio is below the industry average, suggesting it relies more on financing compared to investments relative to its peers. Influencing factors might include:")
    print("- The company might be in a phase where it is raising capital for future investments or to strengthen its financial position.")
    print("- Limited internal cash reserves or operational cash flow, making the company more reliant on external sources of funds.")
    print("- It could be undertaking share repurchases, debt repayments, or dividend distributions leading to higher financing cash outflows.")
    print("- The company might be facing challenges in generating returns from its past investments, causing a hesitancy to invest further.")
