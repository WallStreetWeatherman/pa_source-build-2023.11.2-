import numpy as np
import json

def forecast_values(initial_value, growth_rate, confidence=0.05, years=5):
    forecasted_values = [initial_value]
    for year in range(years):
        next_value = forecasted_values[-1] * (1 + growth_rate / 100)
        forecasted_values.append(next_value)
    return forecasted_values[1:]

# Hard-coded average growth rates (replace these with your actual data)
avg_growth_rate = {
    'Operating Income': -27.98,
    'Depreciation': -2.21,
    'CapEx': 150.85,
    'Working Capital': -332.82,
    'Interest Expense': -31.64
}

last_known_metrics = {
    'Operating Income': 1681.00,
    'Depreciation': 620.00,
    'CapEx': 888.00,
    'Working Capital': -454.00,
    'Interest Expense': 175.00
}

linear_forecasts = {}
weighted_forecasts = {}
combined_forecasts = {}

try:
    with open('past_forecasts.json', 'r') as f:
        past_forecasts = json.load(f)
except FileNotFoundError:
    past_forecasts = {}

for metric, growth_rate in avg_growth_rate.items():
    linear_forecasts[metric] = forecast_values(last_known_metrics[metric], growth_rate)
    past_forecasts[metric] = {'Linear': linear_forecasts[metric]}
    
    weighted_growth_rate = 0.7 * growth_rate + 0.3 * growth_rate
    weighted_forecasts[metric] = forecast_values(last_known_metrics[metric], weighted_growth_rate)
    past_forecasts[metric]['Weighted'] = weighted_forecasts[metric]
    
    combined_forecasts[metric] = [(linear + weighted) / 2 for linear, weighted in zip(linear_forecasts[metric], weighted_forecasts[metric])]
    past_forecasts[metric]['Combined'] = combined_forecasts[metric]
    
    # Handle negative values for growth rate calculations
    sign = np.sign(last_known_metrics[metric])
    
    linear_avg_growth = ((abs(linear_forecasts[metric][-1]) / abs(last_known_metrics[metric])) ** (1/5) - 1) * 100 * sign
    weighted_avg_growth = ((abs(weighted_forecasts[metric][-1]) / abs(last_known_metrics[metric])) ** (1/5) - 1) * 100 * sign
    combined_avg_growth = ((abs(combined_forecasts[metric][-1]) / abs(last_known_metrics[metric])) ** (1/5) - 1) * 100 * sign

    print(f"5-Year Average Growth Rates for {metric}:")
    print(f"  - Linear: {linear_avg_growth:.2f}%")
    print(f"  - Weighted: {weighted_avg_growth:.2f}%")
    print(f"  - Combined: {combined_avg_growth:.2f}%")
    print()

with open('past_forecasts.json', 'w') as f:
    json.dump(past_forecasts, f)
