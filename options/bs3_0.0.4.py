# Bjerksund-Stensland American Option Pricing Model

import math
import numpy as np

def bjerksund_stensland_2002(S, K, r, T, sigma, q, option_type='call'):
    """
    Calculate the American option price using Bjerksund-Stensland 2002 model.
    
    Parameters:
        S (float) - Current stock price
        K (float) - Strike price
        r (float) - Risk-free rate (annualized)
        T (float) - Time to expiration (in years)
        sigma (float) - Volatility of the underlying stock (annualized)
        q (float) - Dividend yield (annualized)
        option_type (str) - 'call' for call option, 'put' for put option
        
    Returns:
        float: American option price
    """

    alpha = 0.5 * ((-r + q + sigma ** 2) - math.sqrt((r - q - sigma ** 2) ** 2 + 2 * sigma ** 2 * r))
    beta = (-0.5 * ((-r + q + sigma ** 2) + math.sqrt((r - q - sigma ** 2) ** 2 + 2 * sigma ** 2 * r)))

    phi = (-beta + np.sqrt(beta ** 2 - 4 * alpha)) / (2 * alpha)
    
    B1 = ((phi - 1) / phi) * K
    B2 = K / (phi - 1)
    A = alpha * (B2 - B1) * (B1) ** phi
    
    if option_type == 'call':
        if S >= B2:
            return S - K
        elif B1 <= S < B2:
            return A * (S - B1)**phi - (S - B1) * B1 + B1 - K
        else:
            return 0
    else:  # Put option
        # Use put-call parity for American options
        call_price = bjerksund_stensland_2002(S, K, r, T, sigma, q, 'call')
        put_price = call_price + K * np.exp(-r * T) - S * np.exp(-q * T)
        return put_price

# Test the function
S = 11.32  # Current stock price
K = 9.0  # Strike price
r = 0.017702  # Risk-free rate
T = 2  # Time to expiration in years
sigma = 0.4695  # Volatility
q = 0.055  # Dividend yield

# Calculate American call option price
call_option_price = bjerksund_stensland_2002(S, K, r, T, sigma, q, 'call')
print(f"The American call option price using Bjerksund-Stensland 2002 model is: ${call_option_price:.2f}")

# Calculate American put option price
put_option_price = bjerksund_stensland_2002(S, K, r, T, sigma, q, 'put')
print(f"The American put option price using Bjerksund-Stensland 2002 model is: ${put_option_price:.2f}")
