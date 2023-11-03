def calculate_total_liabilities(total_current_liabilities, long_term_debt, capital_leases, other_non_current_liabilities):
    total_liabilities = total_current_liabilities + long_term_debt + capital_leases + other_non_current_liabilities
    return total_liabilities

# Given financial data for Book Value of Total Liabilities (in millions)
total_current_liabilities = 66.55  # 66.55 Million
long_term_debt = 0  # 0 Million
capital_leases = 3.25  # 3.25 Million
other_non_current_liabilities = 0.01  # 0.01 Million

# Calculate the Book Value of Total Liabilities
total_liabilities = calculate_total_liabilities(total_current_liabilities, long_term_debt, capital_leases, other_non_current_liabilities)

# Display the Book Value of Total Liabilities
print(f"Book Value of Total Liabilities: {total_liabilities} Million $")
