import numpy as np

# Stage 1: High-Growth Phase
initial_cash_flow = 1_000_000  # Initial free cash flow in dollars
high_growth_rate = 0.15  # High growth rate of 15%
high_growth_years = 5  # High growth period lasts for 5 years
high_discount_rate = 0.10  # Discount rate during the high growth phase

# Stage 2: Stable-Growth Phase
stable_growth_rate = 0.04  # Stable growth rate of 4%
stable_growth_years = 5  # Stable growth period lasts for 5 years
stable_discount_rate = 0.08  # Discount rate during the stable growth phase

# List to store projected and discounted cash flows
future_cash_flows = []
discounted_cash_flows = []

# High-Growth Phase
for i in range(1, high_growth_years + 1):
    future_cash_flow = initial_cash_flow * ((1 + high_growth_rate) ** i)
    discounted_cash_flow = future_cash_flow / ((1 + high_discount_rate) ** i)
    future_cash_flows.append(future_cash_flow)
    discounted_cash_flows.append(discounted_cash_flow)

# Last cash flow in the high-growth phase
last_high_growth_cash_flow = future_cash_flows[-1]

# Stable-Growth Phase
for i in range(1, stable_growth_years + 1):
    future_cash_flow = last_high_growth_cash_flow * ((1 + stable_growth_rate) ** i)
    discounted_cash_flow = future_cash_flow / ((1 + stable_discount_rate) ** (i + high_growth_years))
    future_cash_flows.append(future_cash_flow)
    discounted_cash_flows.append(discounted_cash_flow)

# Terminal Value
# Using the Perpetuity Growth Model to estimate Terminal Value
terminal_value = future_cash_flows[-1] * (1 + stable_growth_rate) / (stable_discount_rate - stable_growth_rate)
discounted_terminal_value = terminal_value / ((1 + stable_discount_rate) ** (high_growth_years + stable_growth_years))

# Total Intrinsic Value
total_intrinsic_value = np.sum(discounted_cash_flows) + discounted_terminal_value

print("Projected Future Cash Flows:")
for i, cash_flow in enumerate(future_cash_flows):
    print(f"Year {i+1}: ${cash_flow:,.2f}")

print("\nDiscounted Future Cash Flows:")
for i, discounted_cash_flow in enumerate(discounted_cash_flows):
    print(f"Year {i+1}: ${discounted_cash_flow:,.2f}")

print(f"\nDiscounted Terminal Value: ${discounted_terminal_value:,.2f}")
print(f"\nTotal Estimated Intrinsic Value: ${total_intrinsic_value:,.2f}")
