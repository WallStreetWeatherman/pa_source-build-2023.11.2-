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

    alpha = 0.5 * ((r - q) * T - (sigma ** 2) * T)
    beta = -0.5 * ((r - q) * T + (sigma ** 2) * T)

    phi = (-beta + np.sqrt(beta ** 2 - 4 * alpha)) / (2 * alpha)

    B1 = ((phi - 1) / phi) * K
    B2 = ((phi / (phi - 1)) * K) / (phi / (phi - 1) - 1)

    A = (B2 - B1) * (phi - 1) / phi
    B = alpha * (B2 - B1) * (B1 / (phi - 1)) ** phi
    C = K - B1 - B

    if option_type == 'call':
        if S >= B2:
            return S - K
        elif B1 < S < B2:
            return A * (S - B1)**phi - B * (S - B1) - C
        else:
            return K - S
    else:  # Put option
        S_prime = K
        K_prime = S
        q_prime = r
        r_prime = q
        call_price = bjerksund_stensland_2002(S_prime, K_prime, r_prime, T, sigma, q_prime, 'call')
        put_price = call_price - S_prime * np.exp(-q_prime * T) + K_prime * np.exp(-r_prime * T)
        return put_price

# Test the function
S = 11.32  # Current stock price
K = 9.0  # Strike price
r = 0.017702  # Risk-free rate
T = 1  # Time to expiration in years
sigma = 0.4695  # Volatility
q = 0.055  # Dividend yield

# Calculate American call option price
call_option_price = bjerksund_stensland_2002(S, K, r, T, sigma, q, 'call')
print(f"The American call option price using Bjerksund-Stensland 2002 model is: ${call_option_price:.2f}")

# Calculate American put option price
put_option_price = bjerksund_stensland_2002(S, K, r, T, sigma, q, 'put')
print(f"The American put option price using Bjerksund-Stensland 2002 model is: ${put_option_price:.2f}")
