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
from scipy.stats import norm

def bjerksund_stensland_call(S, K, r, T, sigma, q):
    # Required functions and parameters
    N = norm.cdf
    b = r - q
    beta = (0.5 - b / sigma**2) + math.sqrt((b / sigma**2 - 0.5)**2 + 2 * r / sigma**2)

    # Defining the alpha function
    def alpha(beta, S, K, r, T):
        return (K * (1 - math.exp(-r * T))) / (beta - 1)

    # Defining the trigger price
    def trigger_price(h, S, beta, K, b, r):
        I1 = alpha(beta, S, K, r, T) + (h - alpha(beta, S, K, r, T)) * math.exp(-b * T)
        return I1

    # Calculating lambda, d1 and d2 for phi function
    def lambda_d1_d2(S, K, T, r, b, sigma):
        lambd = (-(b + 2 * sigma * math.sqrt(T)) + 2 * b) / (2 * sigma**2)
        d1 = -(math.log(S / K) + (b - sigma**2 / 2) * T) / (sigma * math.sqrt(T))
        d2 = d1 - 2 * math.log(S / K) / (sigma * math.sqrt(T))
        return lambd, d1, d2

    # Defining the phi function
    def phi(S, T, gamma, h, I):
        lambd, d1, d2 = lambda_d1_d2(S, K, T, r, b, sigma)
        result = math.exp(-r * T) * (N(d1 - 2 * math.log(I / S) / (sigma * math.sqrt(T))) -
                 (I / S)**(2 * gamma) * N(d2 - 2 * math.log(I / S) / (sigma * math.sqrt(T))))
        return result

    # Calculating the required components
    h = trigger_price(alpha(beta, S, K, r, T), S, beta, K, b, r)
    I = trigger_price(h, S, beta, K, b, r)

    # Putting it all together for the call option
    call = (
    (alpha(beta, S, K, r, T) - K) * (
        S * N(math.log(alpha(beta, S, K, r, T) / S) / (sigma * math.sqrt(T)) + 0.5 * sigma * math.sqrt(T)) - 
        K * N(math.log(alpha(beta, S, K, r, T) / S) / (sigma * math.sqrt(T)) - 0.5 * sigma * math.sqrt(T))
    ) 
    - (
        (alpha(beta, S, K, r, T) - h) * (
            S * N(math.log(alpha(beta, S, K, r, T) / h) / (sigma * math.sqrt(T)) + 0.5 * sigma * math.sqrt(T)) -
            K * N(math.log(alpha(beta, S, K, r, T) / h) / (sigma * math.sqrt(T)) - 0.5 * sigma * math.sqrt(T))
        )
    )
    + phi(S, T, 1, h, I) - phi(S, T, 1, K, I)
)

    return call

def bjerksund_stensland_put(S, K, r, T, sigma, q):
    call_price = bjerksund_stensland_call(S, K, r, T, sigma, q)
    return call_price + K * np.exp(-r * T) - S * np.exp(-q * T)

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