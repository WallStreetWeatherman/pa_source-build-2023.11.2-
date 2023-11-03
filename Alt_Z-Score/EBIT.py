def calculate_ebit(revenue, cogs, operating_expenses):
    ebit = revenue + cogs + operating_expenses  # Note the use of '+' since costs are negative
    return ebit

# Given financial data in millions
revenue = 710.72  # 710.72 Million $
cogs = -140.35    # -140.35 Million $ (negative because it's an expense)
operating_expenses = -620.14  # -620.14 Million $ (negative because it's an expense)

# Calculate EBIT
ebit = calculate_ebit(revenue, cogs, operating_expenses)

# Display EBIT
print(f"Earnings Before Interest and Tax (EBIT): {ebit} Million $")
