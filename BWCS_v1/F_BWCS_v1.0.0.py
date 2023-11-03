import numpy as np

def calculate_scenarios(base_value, historical_values):
    # Calculate the mean and standard deviation of historical values
    mean_value = np.mean(historical_values)
    std_dev = np.std(historical_values)

    # Calculate best and worst-case scenarios
    # Here, we use one standard deviation from the mean for demonstration
    best_case = mean_value + std_dev
    worst_case = mean_value - std_dev

    # Adjust the best and worst-case values based on the base value
    best_case = base_value * (best_case / mean_value)
    worst_case = base_value * (worst_case / mean_value)

    return best_case, worst_case

# Your base case (let's assume it's a revenue forecast for next year in $ million)
base_revenue = 710.72

# Historical revenues for past 5 years (in $ million)
historical_revenues = [26.68, 82.56, 148.76, 271.88, 526.92]

# Calculate best and worst-case scenarios
best_case, worst_case = calculate_scenarios(base_revenue, historical_revenues)

print(f"Best-case scenario: ${best_case:.2f} million")
print(f"Worst-case scenario: ${worst_case:.2f} million")
