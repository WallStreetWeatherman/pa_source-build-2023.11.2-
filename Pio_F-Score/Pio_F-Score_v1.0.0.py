def calculate_piotroski_f_score(net_income, return_on_assets, operating_cash_flow, cash_flow_greater_than_net_income,
                                lower_long_term_debt, higher_current_ratio, no_new_shares,
                                higher_gross_margin, higher_asset_turnover):
    
    f_score = 0
    
    # Profitability tests
    f_score += 1 if net_income > 0 else 0
    f_score += 1 if return_on_assets > 0 else 0
    f_score += 1 if operating_cash_flow > 0 else 0
    f_score += 1 if cash_flow_greater_than_net_income else 0
    
    # Leverage, liquidity, and solvency tests
    f_score += 1 if lower_long_term_debt else 0
    f_score += 1 if higher_current_ratio else 0
    f_score += 1 if no_new_shares else 0
    
    # Operating efficiency tests
    f_score += 1 if higher_gross_margin else 0
    f_score += 1 if higher_asset_turnover else 0
    
    return f_score

# Example usage
net_income = -46_970_000
return_on_assets = -8.1
operating_cash_flow = 25_580_000
cash_flow_greater_than_net_income = True  # Operating cash flow > Net income
lower_long_term_debt = True  # Lower long-term debt this year compared to last year
higher_current_ratio = False  # Higher current ratio this year compared to last year
no_new_shares = False  # No new shares issued this year
higher_gross_margin = True  # Higher gross margin this year compared to last year
higher_asset_turnover = True  # Higher asset turnover ratio this year compared to last year

f_score = calculate_piotroski_f_score(net_income, return_on_assets, operating_cash_flow, cash_flow_greater_than_net_income,
                                      lower_long_term_debt, higher_current_ratio, no_new_shares,
                                      higher_gross_margin, higher_asset_turnover)

print(f"The Piotroski F-Score is: {f_score}")

# Interpretation
if f_score >= 8:
    print("The company is likely to be strong.")
elif 4 <= f_score < 8:
    print("The company's financials are moderate.")
else:
    print("The company is likely to be weak.")