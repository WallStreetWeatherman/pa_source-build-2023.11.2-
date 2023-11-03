# Define the financial metrics with your real numbers
working_capital = 320.07e6  # in dollars, 320.07M
total_assets = 389.88e6  # in dollars, 389.88M
retained_earnings = -361.85e6  # in dollars, -361.85M
earnings_before_interest_and_tax = -49.76e6  # in dollars, -49.76M
market_value_of_equity = 1426.49e6  # in dollars, 1426.49M
book_value_of_total_liabilities = 69.81e6  # in dollars, 69.81M
sales = 710.72e6  # in dollars, 710.72M

# Calculate Altman Z-score components
X1 = working_capital / total_assets
X2 = retained_earnings / total_assets
X3 = earnings_before_interest_and_tax / total_assets
X4 = market_value_of_equity / book_value_of_total_liabilities
X5 = sales / total_assets

# Calculate Altman Z-score
Z_score = 1.2 * X1 + 1.4 * X2 + 3.3 * X3 + 0.6 * X4 + 1.0 * X5

# Print the Altman Z-score
print(f"Altman Z-score: {Z_score}")
