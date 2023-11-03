# Real Options Valuation - Option to Expand using Monte Carlo Simulation
#
# Overview:
# The Real Options Valuation model evaluates the value of potential decisions a company 
# might make in the future. This script simulates multiple future paths for an underlying 
# factor (like market demand) to evaluate an option to expand.
#
# Desired Value:
# A positive value suggests that exercising the option (e.g., expanding) adds shareholder value.

import numpy as np

def monte_carlo_ROV(initial_investment, drift, volatility, risk_free_rate, time_to_exercise, n_simulations=10000):
    dt = time_to_exercise
    option_values = []

    for _ in range(n_simulations):
        # Simulate a random path using geometric Brownian motion
        random_walk = np.exp((drift - 0.5 * volatility**2) * dt + volatility * np.sqrt(dt) * np.random.normal())
        
        # Simulate payoff based on the random path
        simulated_payoff = initial_investment * random_walk

        # Option value at the future time node (exercise if the payoff is positive)
        option_value_at_t = max(simulated_payoff - initial_investment, 0)
        
        # Discount it back to present
        discounted_option_value = option_value_at_t * np.exp(-risk_free_rate * time_to_exercise)
        
        option_values.append(discounted_option_value)

    # Average all simulated option values
    expected_option_value = np.mean(option_values)

    # Convert value to millions format
    option_value_millions = expected_option_value / 1_000_000
    return option_value_millions

# Hardcoded values
initial_investment = 50_000_000  # Example: Initial projected value of the project
drift = 0.07  # Expected annual growth rate of the underlying factor
volatility = 0.2  # Volatility of the underlying factor
risk_free_rate = 0.05  # 5% risk-free rate
time_to_exercise = 1  # Option can be exercised in 1 year

option_value = monte_carlo_ROV(initial_investment, drift, volatility, risk_free_rate, time_to_exercise)
print(f"Option to Expand Value (in millions): ${option_value:.2f}")

# Ensure to further refine and consult with experts for real-world applications.
