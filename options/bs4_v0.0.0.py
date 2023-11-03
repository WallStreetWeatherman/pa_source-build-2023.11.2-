import math
from scipy.stats import norm

def bjerksund_stensland_call(S, K, r, T, sigma, q):
    # Calculating required parameters
    alpha = (-(r - q) * 0.5 + sigma**2 * 0.5 - math.sqrt((r - q - sigma**2) ** 2 + 2 * sigma**2 * r)) / sigma**2
    beta = (1 / 2) - (r - q) / (sigma**2) + math.sqrt((r - q - sigma**2) ** 2 + 2 * r * sigma**2) / (2 * sigma**2)
    lambd = (-r + q + sigma**2 / 2) * T
    d1 = -(math.log(S / K) + (r - q + sigma**2 / 2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)
    I = B0 + (Binf - B0) * (1 - math.exp(lambd))
    h1 = -(r - q) * T + 2 * sigma * math.sqrt(T)
    
    # Call pricing formula
    call_price = S * math.exp(-q * T) * (1 - norm.cdf(d1)) - K * math.exp(-r * T) * (1 - norm.cdf(d2))
    
    if S < I:
        call_price = K - S
    else:
        B0 = K / (1 + alpha)
        Binf = B0 * (beta / (beta - 1))
        h2 = (-(r - q) * T - 2 * sigma * math.sqrt(T)) * (B0 / (Binf - B0))
        if S < h1:
            call_price = (alpha * S - alpha * B0) * S ** beta
        elif S < h2:
            call_price = (alpha * S - alpha * B0) * S ** beta - (alpha * S - alpha * I) * (S - I)
            
    return call_price

# Example
S = 100
K = 100
r = 0.05
T = 1
sigma = 0.2
q = 0

print(bjerksund_stensland_call(S, K, r, T, sigma, q))
