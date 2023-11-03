import numpy as np
import matplotlib.pyplot as plt

def analyze_growth(revenues, profit_margins, roi, debt_to_equity):
    # Filter out 'n/a' values and calculate year-over-year growth rates for revenues
    filtered_revenues = [rev for rev in revenues if rev != 'n/a']
    growth_rates = [(filtered_revenues[i] - filtered_revenues[i-1]) / filtered_revenues[i-1] 
                    for i in range(1, len(filtered_revenues))]

    # Filter out 'n/a' values for other metrics and calculate their means
    filtered_profit_margins = [pm for pm in profit_margins if pm != 'n/a']
    filtered_roi = [r for r in roi if r != 'n/a']
    filtered_debt_to_equity = [de for de in debt_to_equity if de != 'n/a']

    mean_growth = np.mean(growth_rates)
    profit_margin_adj = np.mean(filtered_profit_margins)
    roi_adj = np.mean(filtered_roi)
    debt_to_equity_adj = np.mean(filtered_debt_to_equity)

    # Adjust the mean growth rates based on other parameters
    mean_high_growth_adj = mean_growth * (1 + profit_margin_adj + roi_adj - debt_to_equity_adj)
    mean_stable_growth_adj = mean_growth * (1 - debt_to_equity_adj)

    return mean_high_growth_adj, mean_stable_growth_adj

# in millions
# Historical data for past N years
# Replace these lists with your own data
historical_revenues = ['n/a', 'n/a', 'n/a', 'n/a', 26.68, 82.56, 148.76, 271.88, 526.92, 710.72]
historical_profit_margins = [0.1, 0.12, 'n/a', 0.13, 'n/a', 'n/a', 0.16, 'n/a', 0.16, 0.16]
historical_roi = [0.08, 0.1, 'n/a', 'n/a', 0.11, 0.1, 'n/a', 0.08, 0.07, 0.06]
historical_debt_to_equity = ['n/a', 'n/a', 'n/a', 0.38, 0.35, 0.3, 0.28, 'n/a', 'n/a', 0.18]

# Analyze the data to find high-growth and stable-growth phases
mean_high_growth, mean_stable_growth = analyze_growth(historical_revenues, historical_profit_margins, historical_roi, historical_debt_to_equity)

# Print the mean high-growth and stable-growth rates, adjusted for other factors
print(f"Adjusted Mean High-Growth Rate: {mean_high_growth:.2f}")
print(f"Adjusted Mean Stable-Growth Rate: {mean_stable_growth:.2f}")

# Optional: Plot the historical revenue data (ignoring 'n/a' values)
plt.plot([rev for rev in historical_revenues if rev != 'n/a'])
plt.xlabel("Year")
plt.ylabel("Revenue in $ Million")
plt.title("Historical Revenue Data")
plt.show()
