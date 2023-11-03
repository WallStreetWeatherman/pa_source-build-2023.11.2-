# Cash Flow Return on Investment (CFROI) Calculator
# -------------------------------------------------
# Overview:
# CFROI provides an indication of the company's efficiency at allocating its capital to profitable investments.
# It represents the cash returns to the capital invested in the business.
#
# Formula:
# CFROI = (Operating Cash Flow / Capital Invested) * 100
#
# Desired Value:
# A higher CFROI is preferable, as it indicates that for every dollar of capital invested in the business,
# a larger amount of cash is generated. A lower CFROI might suggest inefficiencies or over-investment without 
# adequate returns.

# Convert amounts where 1 million dollars is represented as 1.00, 10 million as 10.00, etc.
def convert_to_actual_value(value_in_millions):
    return value_in_millions * 1000000

# Hard-coded values for the company

# Operating Cash Flow (in million dollars format for simplicity)
operating_cash_flow_in_millions = 1583.00  # Cash from Operations in Tikr
operating_cash_flow = convert_to_actual_value(operating_cash_flow_in_millions)

# Capital Invested (in million dollars format for simplicity)
capital_invested_in_millions = 200.00 
capital_invested = convert_to_actual_value(capital_invested_in_millions)

# Hard-coded values for the competitor

# Competitor's Operating Cash Flow (in million dollars format for simplicity)
competitor_operating_cash_flow_in_millions = 1500.00  
competitor_operating_cash_flow = convert_to_actual_value(competitor_operating_cash_flow_in_millions)

# Competitor's Capital Invested (in million dollars format for simplicity)
competitor_capital_invested_in_millions = 210.00  
competitor_capital_invested = convert_to_actual_value(competitor_capital_invested_in_millions)

# Calculate CFROI for the company and the competitor
cfroi = (operating_cash_flow / capital_invested) * 100
competitor_cfroi = (competitor_operating_cash_flow / competitor_capital_invested) * 100

# Output the results
print(f"Company's Cash Flow Return on Investment (CFROI): {cfroi:.2f}%")
print(f"Competitor's Cash Flow Return on Investment (CFROI): {competitor_cfroi:.2f}%")

if cfroi >= 25:
    print("The company has a strong CFROI, indicating efficient capital allocation to profitable ventures.")
    if cfroi > competitor_cfroi:
        print("Impressively, the company outperforms its key competitor in terms of CFROI.")
    else:
        print("However, the company lags behind its key competitor in CFROI. It might be beneficial to analyze the competitor's strategies.")
elif cfroi >= 10:
    print("The company has a moderate CFROI. While it's generating returns on investments, there's potential for enhancement.")
    if cfroi > competitor_cfroi:
        print("Notably, the company surpasses its main competitor in terms of CFROI.")
    else:
        print("However, the company's CFROI is lower than its main competitor's. Further assessment is advisable.")
else:
    print("The company displays a low CFROI, which points to possible inefficiencies or challenges in obtaining cash returns from its investments. Comparing against its competitor can offer deeper insights.")
