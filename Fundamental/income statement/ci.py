# Comprehensive Income Calculator
# -------------------------------
# Overview:
# Comprehensive Income represents the total change in a company's equity over a period of time, 
# excluding any changes arising from transactions with its owners like stock issuance or dividends. 
# It accounts for items not included in the traditional net income, such as unrealized gains/losses and 
# foreign currency translation adjustments.
#
# Formula:
# Comprehensive Income = Net Income + Other Comprehensive Income
# Where,
# Other Comprehensive Income = Foreign Currency Translation Gains/Losses + Unrealized Gains/Losses on Available-for-Sale Securities
#
# Desired Value:
# Comprehensive income provides a holistic view of a company's financial performance, 
# capturing all sources of equity change. A higher value indicates a positive change in equity 
# considering both regular business operations and other factors.
#
# Note: This script uses hard-coded values for demonstration. For real-world applications, 
# actual financial data values should be input.

# Hard-coded values in millions as decimals (e.g., 1.00 is $1 million)

# Net Income for the period (in $1M)
net_income = 5.00  # Example value representing $5 million

# Foreign Currency Translation Gains/Losses for the period (in $1M)
foreign_currency_translation = -0.50  # Example value representing a loss of $0.5 million

# Unrealized Gains/Losses on Available-for-Sale Securities for the period (in $1M)
unrealized_gains_losses = 1.00  # Example value representing a gain of $1 million

# Calculate Other Comprehensive Income
other_comprehensive_income = foreign_currency_translation + unrealized_gains_losses

# Calculate Comprehensive Income
comprehensive_income = net_income + other_comprehensive_income

# Output the results
print(f"Net Income (in $1M): ${net_income:.2f}M")
print(f"Foreign Currency Translation (in $1M): ${foreign_currency_translation:.2f}M")
print(f"Unrealized Gains/Losses on Securities (in $1M): ${unrealized_gains_losses:.2f}M")
print(f"Comprehensive Income (in $1M): ${comprehensive_income:.2f}M")
print("Comprehensive Income gives a complete view of the financial performance, including non-operating and non-cash items.")

