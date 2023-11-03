import math
from scipy.stats import norm

# Black-Scholes European Option Pricing Model
# This script calculates the price of a European option using the Black-Scholes model.
# If you're a seller, you generally want the option price to be high for maximum profit.
# If you're a buyer, you'd prefer the option price to be low to get a better deal.

def black_scholes(S, X, T, r, sigma, option_type="call"):
    """Compute the Black-Scholes price for a European option."""
    
    d1 = (math.log(S / X) + (r + 0.5 * sigma**2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)
    
    if option_type == "call":
        option_price = S * norm.cdf(d1) - X * math.exp(-r * T) * norm.cdf(d2)
    elif option_type == "put":
        option_price = X * math.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    else:
        raise ValueError("Invalid option type. Use 'call' or 'put'.")
    
    return option_price

def main():
    # Hard-coded values
    S = 100.0       # Current stock price
    X = 110.0       # Strike price
    T = 1.0         # Time to expiration in years
    r = 0.05        # Risk-free rate (eg, 0.05 for 5%)
    sigma = 0.2     # Volatility
    option_type = "call"  # Option type ('call' or 'put')
    
    option_price = black_scholes(S, X, T, r, sigma, option_type)
    
    print(f"The Black-Scholes {option_type} option price is: ${option_price:.2f}")
    
    # Factors Influencing Output
    print("Factors that might influence this output:")
    if option_type == "call":
        if S > X:
            print("  - The stock is currently trading above the strike price, which is favorable for call options.")
        else:
            print("  - The stock is currently trading below the strike price, which is generally unfavorable for call options.")
    elif option_type == "put":
        if S < X:
            print("  - The stock is currently trading below the strike price, which is favorable for put options.")
        else:
            print("  - The stock is currently trading above the strike price, which is generally unfavorable for put options.")
    
    if r > 0:
        print(f"  - A positive risk-free rate of {r} can contribute to a higher option price.")
    else:
        print("  - A zero or negative risk-free rate can contribute to a lower option price.")
    
    if sigma > 0.2:
        print("  - The stock is highly volatile, which increases the option's price.")
    else:
        print("  - The stock has low volatility, generally resulting in a lower option price.")

    if T > 1:
        print("  - The option has a longer time until expiration, generally increasing its price.")
    else:
        print("  - The option has a shorter time until expiration, generally decreasing its price.")

if __name__ == "__main__":
    main()