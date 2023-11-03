import math
from scipy.stats import norm

def whaley(S, K, r, q, T, sigma):
    """Compute the Whaley approximation price for an American call option with dividends."""
    
    # European option calculations
    d1 = (math.log(S / K) + (r - q + 0.5 * sigma**2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)

    N_d1 = norm.cdf(d1)
    N_d2 = norm.cdf(d2)

    # Calculate European option price
    european_price = S * math.exp(-q * T) * N_d1 - K * math.exp(-r * T) * N_d2

    # Early exercise premium calculations
    d1_div = (math.log(S / K) + (r - q + 0.5 * sigma**2) * (T - T)) / (sigma * math.sqrt(T - T))  # Assuming dividend at T
    d2_div = d1_div - sigma * math.sqrt(T - T)

    N_minus_d2_div = norm.cdf(-d2_div)
    
    early_exercise_premium = math.exp(-r * T) * (K * N_minus_d2_div - S * math.exp(-q * T))
    
    return european_price + early_exercise_premium

def main():
    # Hard-coded values
    S = 100.0       # Current stock price
    K = 110.0       # Strike price
    T = 1.0         # Time to expiration in years
    r = 0.05        # Risk-free rate (e.g., 0.05 for 5%)
    q = 0.03        # Dividend yield (e.g., 0.03 for 3%)
    sigma = 0.2     # Volatility
    
    option_price = whaley(S, K, r, q, T, sigma)
    
    print(f"The Whaley option price is: ${option_price:.2f}")

if __name__ == "__main__":
    main()
