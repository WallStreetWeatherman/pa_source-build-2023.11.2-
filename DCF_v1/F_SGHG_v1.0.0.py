import numpy as np
import matplotlib.pyplot as plt

def analyze_growth(revenues, profit_margins, roi, debt_to_equity):
    # Calculate year-over-year growth rates for revenues
    growth_rates = [(revenues[i] - revenues[i-1]) / revenues[i-1] for i in range(1, len(revenues))]

    # Calculate the mean and standard deviation of the growth rates
    mean_growth = np.mean(growth_rates)
    std_dev_growth = np.std(growth_rates)

    # Initialize variables to hold high-growth and stable-growth phases
    high_growth_phase = []
    stable_growth_phase = []

    # Initialize adjustment factors
    profit_margin_adj = np.mean(profit_margins)
    roi_adj = np.mean(roi)
    debt_to_equity_adj = np.mean(debt_to_equity)

    # Adjust the mean growth rates based on other parameters
    mean_high_growth_adj = mean_growth * (1 + profit_margin_adj + roi_adj - debt_to_equity_adj)
    mean_stable_growth_adj = mean_growth * (1 - debt_to_equity_adj)

    # Output the results
    return mean_high_growth_adj, mean_stable_growth_adj

# Historical data for past N years
# Replace these lists with your own data
historical_revenues = [100, 120, 140, 165, 200, 210, 220, 230, 240, 250]
historical_profit_margins = [0.1, 0.12, 0.15, 0.13, 0.14, 0.15, 0.16, 0.17, 0.16, 0.16]
historical_roi = [0.08, 0.1, 0.12, 0.11, 0.11, 0.1, 0.09, 0.08, 0.07, 0.06]
historical_debt_to_equity = [0.5, 0.45, 0.4, 0.38, 0.35, 0.3, 0.28, 0.25, 0.2, 0.18]

# Analyze the data to find high-growth and stable-growth phases
mean_high_growth, mean_stable_growth = analyze_growth(historical_revenues, historical_profit_margins, historical_roi, historical_debt_to_equity)

# Print the mean high-growth and stable-growth rates, adjusted for other factors
print(f"Adjusted Mean High-Growth Rate: {mean_high_growth:.2f}")
print(f"Adjusted Mean Stable-Growth Rate: {mean_stable_growth:.2f}")

# Optional: Plot the historical revenue data
plt.plot(historical_revenues)
plt.xlabel("Year")
plt.ylabel("Revenue in $ Million")
plt.title("Historical Revenue Data")
plt.show()
