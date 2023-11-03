import numpy as np
import matplotlib.pyplot as plt

def calculate_net_profit_margins(historical_net_profits, historical_revenues):
    """
    Calculate Net Profit Margins for multiple years based on historical Net Profits and Revenues.
    
    Parameters:
        historical_net_profits (list): List of historical Net Profits or Net Incomes (in million).
        historical_revenues (list): List of historical Revenues (in million).
        
    Returns:
        historical_net_profit_margins (list): List of historical Net Profit Margins in percentage.
    """
    if len(historical_net_profits) != len(historical_revenues):
        raise ValueError("Length of historical_net_profits and historical_revenues must be equal.")
    
    historical_net_profit_margins = []
    for net_profit, revenue in zip(historical_net_profits, historical_revenues):
        if net_profit == 'n/a' or revenue == 'n/a':
            historical_net_profit_margins.append('n/a')
            continue
        if revenue != 0:  # To avoid division by zero
            net_profit_margin = (net_profit / revenue) * 100  
        else:
            net_profit_margin = 0.0  # In case revenue is zero
        
        historical_net_profit_margins.append(net_profit_margin)
    
    return historical_net_profit_margins

# Add Variables Here:
historical_net_profits = ['n/a', 'n/a', 'n/a', 'n/a', -75.24, -72.06, -18.11, -107.66, -65.68, -46.97]
historical_revenues = ['n/a', 'n/a', 'n/a', 'n/a', 26.68, 82.56, 148.76, 271.88, 526.92, 710.72]  # in millions
historical_net_profit_margins = calculate_net_profit_margins(historical_net_profits, historical_revenues)

def analyze_growth(revenues, profit_margins, roi, debt_to_equity):
    filtered_revenues = [rev for rev in revenues if rev != 'n/a']
    growth_rates = [(filtered_revenues[i] - filtered_revenues[i-1]) / filtered_revenues[i-1] 
                    for i in range(1, len(filtered_revenues))]
                    
    filtered_profit_margins = [pm for pm in profit_margins if pm != 'n/a']
    filtered_roi = [r for r in roi if r != 'n/a']
    filtered_debt_to_equity = [de for de in debt_to_equity if de != 'n/a']

    mean_growth = np.mean(growth_rates)
    profit_margin_adj = np.mean(filtered_profit_margins)
    roi_adj = np.mean(filtered_roi)
    debt_to_equity_adj = np.mean(filtered_debt_to_equity)

    mean_high_growth_adj = mean_growth * (1 + profit_margin_adj + roi_adj - debt_to_equity_adj)
    mean_stable_growth_adj = mean_growth * (1 - debt_to_equity_adj)

    return mean_high_growth_adj, mean_stable_growth_adj

# Calculate historical profit margins
historical_profit_margins = calculate_net_profit_margins(historical_net_profits, historical_revenues)

# Rest of your historical data
historical_roi = ['n/a', 'n/a', 'n/a', 'n/a', -2.429, -1.535, -0.147, -0.299, -0.209, -0.153]
historical_debt_to_equity = ['n/a', 'n/a', 'n/a', 'n/a', 0.369 , 0.032, 'n/a', 0.016, 0.017, 0.016]

# Analyze the data
mean_high_growth, mean_stable_growth = analyze_growth(historical_revenues, historical_profit_margins, historical_roi, historical_debt_to_equity)

# Output results
print(f"Adjusted Mean High-Growth Rate: {mean_high_growth:.2f}")
print(f"Adjusted Mean Stable-Growth Rate: {mean_stable_growth:.2f}")

# Plotting
plt.plot([rev for rev in historical_revenues if rev != 'n/a'])
plt.xlabel("Year")
plt.ylabel("Revenue in $ Million")
plt.title("Historical Revenue Data")
plt.show()
