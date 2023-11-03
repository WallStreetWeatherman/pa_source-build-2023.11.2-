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
# Representing both net profits and revenues in terms of millions as decimals
historical_net_profits = ['n/a', 'n/a', 'n/a', 'n/a', -75.24, -72.06, -18.11, -107.66, -65.68, -46.97]
historical_revenues = ['n/a', 'n/a', 'n/a', 'n/a', 26.68, 82.56, 148.76, 271.88, 526.92, 710.72]  # in millions

historical_net_profit_margins = calculate_net_profit_margins(historical_net_profits, historical_revenues)

print(f"Historical Net Profit Margins: {historical_net_profit_margins}")
