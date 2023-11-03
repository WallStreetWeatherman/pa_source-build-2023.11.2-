import numpy as np
import matplotlib.pyplot as plt

def merton_jump_diffusion(S0, r, sigma, lam, muJ, sigmaJ, T, dt, num_simulations):
    num_steps = int(T / dt)
    jump_size = np.random.normal(muJ, sigmaJ, (num_simulations, num_steps))
    jump_timing = np.random.poisson(lam * dt, (num_simulations, num_steps))
    
    # Initialize paths
    S = np.zeros((num_simulations, num_steps))
    S[:, 0] = S0

    # Simulate paths
    for t in range(1, num_steps):
        S[:, t] = S[:, t-1] * np.exp((r - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * np.random.normal(0, 1, num_simulations) + jump_size[:, t] * jump_timing[:, t])
    
    return S

def main():
    # Parameters
    S0 = 100               # Initial stock price
    r = 0.05               # Risk-free rate
    sigma = 0.2            # Volatility
    T = 1.0                # Time to maturity
    dt = 0.01              # Time increment
    num_simulations = 10   # Number of simulations

    # Jump parameters
    lam = 1.0              # Jump intensity (expected number of jumps per year)
    muJ = -0.2             # Expected jump size (negative for downward jump)
    sigmaJ = 0.1           # Standard deviation of jump size

    stock_paths = merton_jump_diffusion(S0, r, sigma, lam, muJ, sigmaJ, T, dt, num_simulations)

    # Plot simulations
    plt.figure(figsize=(10, 6))
    for i in range(num_simulations):
        plt.plot(np.linspace(0, T, int(T / dt)), stock_paths[i, :])
    plt.title("Merton's Jump Diffusion Model Stock Price Paths")
    plt.xlabel('Time to Maturity')
    plt.ylabel('Stock Price')
    plt.show()

if __name__ == "__main__":
    main()