import numpy as np
import matplotlib.pyplot as plt

def heston_simulation(S0, v0, T, mu, kappa, theta, sigma, rho, dt, num_simulations):
    # Number of time steps
    num_steps = int(T / dt)
    
    # Arrays to store simulations
    S = np.zeros((num_simulations, num_steps))
    v = np.zeros_like(S)
    S[:, 0] = S0
    v[:, 0] = v0

    # Generate paths
    for t in range(1, num_steps):
        # Generate correlated random numbers
        Z = np.random.normal(0, 1, (num_simulations, 2))
        W1 = Z[:, 0]
        W2 = rho * Z[:, 0] + np.sqrt(1 - rho**2) * Z[:, 1]

        # Euler discretization
        S[:, t] = S[:, t-1] + mu * S[:, t-1] * dt + np.sqrt(v[:, t-1]) * S[:, t-1] * np.sqrt(dt) * W1
        v[:, t] = v[:, t-1] + kappa * (theta - np.maximum(v[:, t-1], 0)) * dt + sigma * np.sqrt(np.maximum(v[:, t-1], 0)) * np.sqrt(dt) * W2
        v[:, t] = np.maximum(v[:, t], 0)  # Ensure variance is non-negative

    return S

def main():
    # Parameters for the Heston model
    S0 = 100               # Initial stock price
    v0 = 0.04              # Initial variance
    T = 1.0                # Time to maturity
    mu = 0.05              # Risk-free rate
    kappa = 2.0            # Mean reversion coefficient
    theta = 0.04           # Long-term variance mean
    sigma = 0.5            # Volatility of volatility
    rho = -0.7             # Correlation coefficient
    dt = 0.01              # Time increment
    num_simulations = 10   # Number of simulations

    # Simulate stock paths
    stock_paths = heston_simulation(S0, v0, T, mu, kappa, theta, sigma, rho, dt, num_simulations)

    # Plot stock paths
    plt.figure(figsize=(10, 6))
    for i in range(num_simulations):
        plt.plot(np.linspace(0, T, int(T / dt)), stock_paths[i, :])
    plt.title('Heston Model Stock Price Paths')
    plt.xlabel('Time to Maturity')
    plt.ylabel('Stock Price')
    plt.show()

if __name__ == "__main__":
    main()