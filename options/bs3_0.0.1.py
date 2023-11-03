import math

def bjerksund_stensland_2002(S, K, r, T, sigma, q):
    """
    Calculate the American option price using Bjerksund-Stensland 2002 model.
    
    Parameters:
        S (float) - Current stock price
        K (float) - Strike price
        r (float) - Risk-free rate (annualized)
        T (float) - Time to expiration (in years)
        sigma (float) - Volatility of the underlying stock (annualized)
        q (float) - Dividend yield (annualized)
        
    Returns:
        float: American call option price
    """

    # Calculate alpha and beta parameters
    alpha = 0.5 * ((r - q) * T - (sigma ** 2) * T)
    beta = -0.5 * ((r - q) * T + (sigma ** 2) * T)

    # Calculate gamma and phi
    gamma = K / ((phi - 1) / phi * K)
    phi = (-beta + math.sqrt(beta ** 2 - 4 * alpha * gamma)) / (2 * alpha)
    
    # Calculate trigger prices B1 and B2
    B1 = ((phi - 1) / phi) * K
    B2 = ((phi / (phi - 1)) * K) / (phi / (phi - 1) - 1)

    # Additional constants for f(S) equation
    A = (B2 - B1) * (phi - 1) / phi
    B = alpha * (B2 - B1) * (B1 / (phi - 1)) ** phi
    C = K - B1 - B
    
    # Option pricing based on different ranges of stock price
    if S >= B2:
        return S - K
    elif B1 < S < B2:
        return A * (S - B1)**phi - B * (S - B1) - C
    else:
        return K - S

# Test the function
S = 11.32  # Current stock price
K = 9.0  # Strike price
r = 0.017702  # Risk-free rate
T = 1  # Time to expiration in years
sigma = 0.4695  # Volatility
q = 0.055  # Dividend yield

# Calculate American option price
option_price = bjerksund_stensland_2002(S, K, r, T, sigma, q)
print(f"The American call option price using Bjerksund-Stensland 2002 model is: ${option_price:.2f}")
