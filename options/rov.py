# Real Options Valuation - Option to Expand using Binomial Model
#
# Overview:
# The Real Options Valuation model focuses on potential decisions a company might make 
# in the future, such as the decision to expand. The model assigns value to these options 
# by considering the potential payoffs and the likelihood of different scenarios.
#
# Desired Value:
# A positive value indicates that the option provides a positive net present value 
# to the company if exercised, thus adding to shareholder value.

import math

def option_to_expand_value(initial_investment, up_payoff, down_payoff, risk_free_rate, volatility, time_to_exercise):
    # Calculate up and down move factors
    u = math.exp(volatility * math.sqrt(time_to_exercise))
    d = 1/u
    
    # Calculate risk-neutral probability
    q = (math.exp(risk_free_rate * time_to_exercise) - d) / (u - d)
    
    # Calculate option values at the future time nodes
    up_option_value = max(up_payoff - initial_investment, 0)
    down_option_value = max(down_payoff - initial_investment, 0)
    
    # Calculate present value of the option
    option_value = math.exp(-risk_free_rate * time_to_exercise) * (q * up_option_value + (1 - q) * down_option_value)

    # Convert value to millions format
    option_value_millions = option_value / 1_000_000
    return option_value_millions

# Hardcoded example values
initial_investment = 50_000_000  # Example: $50 million required to exercise the option (expand)
up_payoff = 80_000_000  # Example: Payoff if things go well (up state)
down_payoff = 30_000_000  # Example: Payoff if things don't go well (down state)
risk_free_rate = 0.05  # 5% risk-free rate
volatility = 0.25  # Estimated volatility of the underlying asset/project
time_to_exercise = 1  # Option can be exercised in 1 year

option_value = option_to_expand_value(initial_investment, up_payoff, down_payoff, risk_free_rate, volatility, time_to_exercise)
print(f"Option to Expand Value (in millions): ${option_value:.2f}")

# Remember to consult with experts and refine the model for real-world scenarios.
