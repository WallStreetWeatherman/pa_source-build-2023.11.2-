# Internal Rate of Return (IRR) Calculation
# -----------------------------------------
# Overview:
# IRR is a metric used in capital budgeting to measure the potential return of an investment. It is the 
# discount rate that makes the net present value (NPV) of cash flows from a particular investment equal to zero.
#
# Desired Value:
# A higher IRR is preferable as it indicates a potentially higher return on investment. It's essential to 
# compare the IRR with the required rate of return or a benchmark rate to decide if the investment is worth pursuing.

import numpy as np

# Hardcoded values (using the format where 1 million is represented as 1.00, 10 million as 10.00, etc.)
# Negative values represent cash outflows, and positive values represent cash inflows.
cash_flows = [-100.00, 30.00, 40.00, 50.00, 60.00]  # E.g., an initial investment of $100 million and subsequent inflows

def calculate_irr(cash_flows):
    """Calculate the internal rate of return."""
    return np.irr(cash_flows) * 100  # Convert to percentage

irr = calculate_irr(cash_flows)

print(f"Cash Flows: {[f'${cf:.2f} million' for cf in cash_flows]}")
print(f"Internal Rate of Return (IRR): {irr:.2f}%")

# Interpretation
benchmark_rate = 8.0  # This can be your company's required rate of return, for instance
if irr > benchmark_rate:
    print(f"The IRR of {irr:.2f}% is greater than the benchmark rate of {benchmark_rate}%, indicating a potentially good investment.")
else:
    print(f"The IRR of {irr:.2f}% is less than or equal to the benchmark rate of {benchmark_rate}%, suggesting caution in pursuing the investment.")
