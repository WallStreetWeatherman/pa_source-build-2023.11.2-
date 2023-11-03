# Net Present Value (NPV) Calculator
# ----------------------------------
# Overview:
# Net Present Value (NPV) is a foundational concept in finance and capital budgeting.
# It measures the profitability of an investment by comparing the present value of expected cash 
# inflows to the initial investment cost. Positive NPV indicates that the investment should 
# increase the value of the firm, while a negative NPV suggests the opposite.
#
# Formula:
# NPV = ∑ [(Cash inflow / (1 + r)^t) - Initial Investment]
# Where:
# r = Discount rate
# t = Time period
# 
# Desired Value:
# A higher NPV indicates a more profitable investment. Ideally, you want this value to be positive.
#
# Note: This script uses hard-coded values for demonstration. For real-world applications,
# actual cash inflows, discount rates, and initial investments should be input.

# Hard-coded values in millions as decimals (e.g., 1.00 is $1 million)

# Initial investment
initial_investment = 11.11  # Stock price

# Forecasted cash inflows for the next 5 years
cash_inflows = [-861.89, -4524.77, -13083.30, -34298.00, -87114.24]  # Use either FCFF or FCFE

# Discount rate (e.g., 10% is 0.10)
discount_rate = 0.10 # WACC

# Calculate NPV
npv = -initial_investment  # start with negative initial investment
for t, cash_inflow in enumerate(cash_inflows, 1):
    npv += cash_inflow / (1 + discount_rate) ** t

# Outputting the results
print(f"Net Present Value (NPV): ${npv:.2f} million")
if npv > 0:
    print("The investment is expected to be profitable.")
else:
    print("The investment is not expected to be profitable.")

