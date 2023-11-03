import numpy as np

def calculate_net_profit_margins(historical_net_profits, historical_revenues):
    if len(historical_net_profits) != len(historical_revenues):
        raise ValueError("Length of historical_net_profits and historical_revenues must be equal.")
    
    historical_net_profit_margins = []
    for net_profit, revenue in zip(historical_net_profits, historical_revenues):
        if net_profit == 'none' or revenue == 'none':
            historical_net_profit_margins.append('none')
            continue
        if revenue != 0:
            net_profit_margin = (net_profit / revenue) * 100  
        else:
            net_profit_margin = 0.0  
        
        historical_net_profit_margins.append(net_profit_margin)
    
    return historical_net_profit_margins

# Initialize Variables
historical_net_profits = ['none', 'none', 'none', 'none', -75.24, -72.06, -18.11, -107.66, -65.68, -46.97]
historical_revenues = ['none', 'none', 'none', 'none', 26.68, 82.56, 148.76, 271.88, 526.92, 710.72]
historical_net_profit_margins = calculate_net_profit_margins(historical_net_profits, historical_revenues)

def analyze_growth(revenues, profit_margins, roi, debt_to_equity):
    filtered_revenues = [rev for rev in revenues if rev != 'none']
    growth_rates = [(filtered_revenues[i] - filtered_revenues[i-1]) / filtered_revenues[i-1] for i in range(1, len(filtered_revenues))]
    filtered_profit_margins = [pm for pm in profit_margins if pm != 'none']
    filtered_roi = [r for r in roi if r != 'none']
    filtered_debt_to_equity = [de for de in debt_to_equity if de != 'none']

    mean_growth = np.mean(growth_rates)
    profit_margin_adj = np.mean(filtered_profit_margins)
    roi_adj = np.mean(filtered_roi)
    debt_to_equity_adj = np.mean(filtered_debt_to_equity)

    mean_high_growth_adj = mean_growth * (1 + profit_margin_adj + roi_adj - debt_to_equity_adj)
    mean_stable_growth_adj = mean_growth * (1 - debt_to_equity_adj)

    return mean_high_growth_adj, mean_stable_growth_adj

def calculate_discount_rates(mean_high_growth_adj, mean_stable_growth_adj, risk_free_rate=0.03):
    high_discount_rate = risk_free_rate + mean_high_growth_adj
    stable_discount_rate = risk_free_rate + mean_stable_growth_adj
    return high_discount_rate, stable_discount_rate

# Additional historical data
historical_roi = ['none', 'none', 'none', 'none', -2.429, -1.535, -0.147, -0.299, -0.209, -0.153]
historical_debt_to_equity = ['none', 'none', 'none', 'none', 0.369, 0.032, 'none', 0.016, 0.017, 0.016]

# Analyze the data
mean_high_growth, mean_stable_growth = analyze_growth(historical_revenues, historical_net_profit_margins, historical_roi, historical_debt_to_equity)

# Calculate discount rates
high_discount_rate, stable_discount_rate = calculate_discount_rates(mean_high_growth, mean_stable_growth)

# Output results
print(f"Adjusted Mean High-Growth Rate: {mean_high_growth:.2f}")
print(f"Adjusted Mean Stable-Growth Rate: {mean_stable_growth:.2f}")
print(f"Estimated High Discount Rate: {high_discount_rate:.2f}")
print(f"Estimated Stable Discount Rate: {stable_discount_rate:.2f}")