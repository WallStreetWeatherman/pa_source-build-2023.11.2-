# Bjerksund-Stensland American Option Pricing Model
# -------------------------------------------------
# This script calculates the price of an American call or put option.
# A high value indicates the option is valuable; a low value suggests it is less valuable.
# Variables to be input: S (stock price), K (strike price), r (risk-free rate),
# T (time to expiration in years), sigma (volatility), dividends (continuous dividend yield)

import math
import scipy.stats as stats

def bjerksund_stensland(S, K, r, T, sigma, dividends, option_type="call"):
    # Helper functions
    def phi(S, T, gamma, H, I, r, sigma):
        kappa = 2 * r / ((sigma ** 2) * (1 - math.exp(-r * T))) * S * math.exp((r + gamma * sigma ** 2) * T)
        lambda_ = (-r + gamma * sigma ** 2 + 2 * sigma ** 2) / ((sigma ** 2) * (1 - math.exp(-r * T)))
        d1 = -(math.log(S / H) + (r + (gamma - 0.5) * sigma ** 2) * T) / (sigma * math.sqrt(T))
        d2 = d1 - 2 * math.log(I / S) / (sigma * math.sqrt(T))
        d3 = d1 - 2 * math.log(I / H) / (sigma * math.sqrt(T))
        return math.exp(-r * T) * (phi_1(d1, lambda_, kappa) - phi_1(d2, 1, kappa) - phi_1(d3, 1 - lambda_, kappa) + phi_1(d3 - 2 * math.log(I / H) / (sigma * math.sqrt(T)), 1, kappa))

    def phi_1(d, gamma, kappa):
        cdf_d = stats.norm.cdf(d)
        if cdf_d - 1 < 0:
            return 0
        return kappa * (cdf_d ** gamma)

    # Parameters for the Bjerksund-Stensland approximation
    beta = (0.5 - dividends / (sigma ** 2)) + math.sqrt((dividends / (sigma ** 2) - 0.5) ** 2 + 2 * r / (sigma ** 2))
    beta_inv = 1 / beta
    B0 = max(K, (r / (r - dividends)) * K)
    Binf = beta / (beta - 1) * K
    hT = -(dividends * T + 2 * sigma * math.sqrt(T)) * K / (Binf - K)
    I = Binf + (B0 - Binf) * math.exp(hT)

    if option_type.lower() == "call":
        # Calculate the American call option price
        alpha = (I - K) * I ** (-beta_inv)
        return phi(S, T, beta, I, I, r, sigma) - K * phi(S, T, beta_inv, I, I, r, sigma) - alpha * (S * phi(S, T, beta, I, B0, r, sigma) - K * phi(S, T, beta_inv, I, B0, r, sigma))

    elif option_type.lower() == "put":
        # Calculate the American put option price directly
        alpha = (I - K) * I ** (-beta_inv)
        return K * phi(S, T, beta_inv, I, I, r, sigma) - S * phi(S, T, beta, I, I, r, sigma) + alpha * (K * phi(S, T, beta_inv, I, B0, r, sigma) - S * phi(S, T, beta, I, B0, r, sigma))


    else:
        return "Invalid option type. Please use 'call' or 'put'."


# Test the function
S = 11.32  # Current stock price
K = 9.0  # Strike price
r = 0.017702  # Risk-free rate
T = 1  # Time to expiration in years
sigma = 0.4695  # Volatility
dividends = 0.055  # Dividend yield

call_price = bjerksund_stensland(S, K, r, T, sigma, dividends, "call")
put_price = bjerksund_stensland(S, K, r, T, sigma, dividends, "put")

print(f"American call option price: {call_price}")
print(f"American put option price: {put_price}")
