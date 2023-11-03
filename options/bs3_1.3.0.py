# Bjerksund-Stensland American Option Pricing Model
# ------------------------------------------------
# Overview:
# This script calculates the price of an American option using the Bjerksund-Stensland model.
# The model provides a numerical approximation for the valuation of American-style options, 
# which can be exercised before expiration. It is an extension to the more commonly known Black-Scholes model
# but tailored for early exercise features.
#
# Desired Value:
# In the realm of options trading, the goal is generally to buy options at a low price and sell at a high price
# for buyers, and vice versa for sellers. A higher option price is usually beneficial for sellers, 
# while a lower option price is more favorable for buyers.

import math
import numpy as np

# Calculate American call option price
def bjerksund_stensland_call(S, K, r, T, sigma, q):
    alpha = 0.5 * ((-r + q + sigma ** 2) - math.sqrt((r - q - sigma ** 2) ** 2 + 2 * sigma ** 2 * r))
    beta = (-0.5 * ((-r + q + sigma ** 2) + math.sqrt((r - q - sigma ** 2) ** 2 + 2 * sigma ** 2 * r)))
    phi = (-beta + np.sqrt(beta ** 2 - 4 * alpha)) / (2 * alpha)
    B1 = ((phi - 1) / phi) * K
    B2 = K / (phi - 1)
    A = alpha * (B2 - B1) * (B1) ** phi

    if S >= B2:
        return np.exp(-r * T) * (S - K)
    elif B1 <= S < B2:
        return np.exp(-r * T) * (A * (S - B1)**phi - (S - B1) * B1 + B1 - K)
    else:
        return 0

# Calculate American put option price
def bjerksund_stensland_put(S, K, r, T, sigma, q):
    call_price = bjerksund_stensland_call(S, K, r, T, sigma, q)
    put_price = call_price + K * np.exp(-r * T) - S * np.exp(-q * T)
    return put_price

# Wrapper function for both call and put
def bjerksund_stensland_2002(S, K, r, T, sigma, q, option_type='call'):
    if option_type == 'call':
        return bjerksund_stensland_call(S, K, r, T, sigma, q)
    else:
        return bjerksund_stensland_put(S, K, r, T, sigma, q)

# Hard-coded values
S = 11.30  # Current stock price
K = 9.0  # Strike price
r = 0.017702  # Risk-free rate
T_days = 365  # Time to expiration in days
T = T_days / 365.0  # Convert time to expiration to years
sigma = 0.4695  # Volatility
q = 0.055  # Dividend yield

# Calculate American call option price
call_option_price = bjerksund_stensland_2002(S, K, r, T, sigma, q, 'call')
print(f"The American call option price using Bjerksund-Stensland 2002 model is: ${call_option_price:.2f}")

# Calculate American put option price
put_option_price = bjerksund_stensland_2002(S, K, r, T, sigma, q, 'put')
print(f"The American put option price using Bjerksund-Stensland 2002 model is: ${put_option_price:.2f}")

# Print statements for condition analysis
if S > K:
    print(f"  - Stock Price (S): The stock is currently trading above the strike price.")
    print(f"    - Good for call options.")
    print(f"    - Bad for put options.")
else:
    print(f"  - Stock Price (S): The stock is currently trading below the strike price.")
    print(f"    - Bad for call options.")
    print(f"    - Good for put options.")

if r > q:
    print(f"  - Risk-Free Rate vs Dividend Yield: The risk-free rate is higher than the dividend yield.")
    print(f"    - Good for call options.")
    print(f"    - Bad for put options.")
else:
    print(f"  - Risk-Free Rate vs Dividend Yield: The dividend yield is higher than the risk-free rate.")
    print(f"    - Bad for call options.")
    print(f"    - Good for put options.")

if sigma > 0.2:
    print(f"  - Volatility (sigma): The stock is highly volatile.")
    print(f"    - Good for both call and put options.")
else:
    print(f"  - Volatility (sigma): The stock has low volatility.")
    print(f"    - Bad for both call and put options.")

if T > 1:
    print(f"  - Time to Expiry (T): The option has a longer time until expiration.")
    print(f"    - Good for both call and put options.")
else:
    print(f"  - Time to Expiry (T): The option has a shorter time until expiration.")
    print(f"    - Bad for both call and put options.")