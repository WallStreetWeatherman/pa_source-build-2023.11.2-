import numpy as np

def explicit_fdm_european_call(S, K, r, T, sigma, M, N):
    """Compute the European call option price using the Explicit Finite Difference Method."""
    
    # Grid initialization
    dt = T/N
    dS = 2*S/M
    lamb = r*dt
    gamma = sigma**2*dt
    prices = np.zeros((M+1, N+1))
    stock_prices = np.linspace(0, 2*S, M+1)

    # Set up boundary conditions
    prices[:, N] = np.maximum(stock_prices - K, 0)
    prices[0, :] = 0
    prices[M, :] = 2*prices[M-1, :] - prices[M-2, :]

    # Backward in time calculation
    for j in range(N-1, -1, -1):
        for i in range(1, M):
            prices[i, j] = prices[i, j+1] + 0.5*gamma*i**2*(prices[i+1, j+1] - 2*prices[i, j+1] + prices[i-1, j+1]) \
                          + 0.5*lamb*i*(prices[i+1, j+1] - prices[i-1, j+1])
    
    # Return the option price at S
    return prices[int(M/2), 0]

def main():
    # Hard-coded values
    S = 100.0       # Current stock price
    K = 110.0       # Strike price
    T = 1.0         # Time to expiration in years
    r = 0.05        # Risk-free rate (e.g., 0.05 for 5%)
    sigma = 0.2     # Volatility
    M = 100         # Number of stock price steps
    N = 100         # Number of time steps
    
    option_price = explicit_fdm_european_call(S, K, r, T, sigma, M, N)
    
    print(f"The European call option price using EFDM is: ${option_price:.2f}")

if __name__ == "__main__":
    main()
