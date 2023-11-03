import numpy as np
import matplotlib.pyplot as plt

def merton_jump_diffusion(S0, r, sigma, lam, mu_j, sigma_j, T, dt, num_simulations):
    """
    Simulate stock prices using Merton's Jump Diffusion model.

    S0: Initial stock price
    r: Risk-free rate
    sigma: Volatility of stock
    lam: Expected number of jumps per unit time
    mu_j: Mean of jump size
    sigma_j: Volatility of jump size
    T: Time to maturity
    dt: Time increment
    num_simulations: Number of simulations
    """
    num_steps = int(T / dt)
    jump_diffusion_paths = np.zeros((num_simulations, num_steps))
    jump_diffusion_paths[:, 0] = S0

    for t in range(1, num_steps):
        # Standard Brownian motion
        dW = np.sqrt(dt) * np.random.randn(num_simulations)
        
        # Poisson process for the number of jumps
        n_jumps = np.random.poisson(lam * dt, num_simulations)
        
        # Calculate jump sizes
        jump_sizes = np.zeros(num_simulations)
        for i in range(num_simulations):
            for _ in range(n_jumps[i]):
                jump_sizes[i] += np.random.normal(mu_j, sigma_j)
        
        # Merton's jump diffusion model
        dS = (r - lam * (np.exp(mu_j + 0.5 * sigma_j**2) - 1)) * jump_diffusion_paths[:, t-1] * dt
        dS += sigma * jump_diffusion_paths[:, t-1] * dW
        dS += jump_diffusion_paths[:, t-1] * (np.exp(jump_sizes) - 1)
        jump_diffusion_paths[:, t] = jump_diffusion_paths[:, t-1] + dS

    return jump_diffusion_paths

def main():
    # Parameters
    S0 = 100
    r = 0.05
    sigma = 0.2
    lam = 0.1
    mu_j = -0.1
    sigma_j = 0.1
    T = 1.0
    dt = 0.01
    num_simulations = 10
    
    jump_diffusion_paths = merton_jump_diffusion(S0, r, sigma, lam, mu_j, sigma_j, T, dt, num_simulations)

    plt.figure(figsize=(10, 6))
    for i in range(num_simulations):
        plt.plot(np.linspace(0, T, int(T / dt)), jump_diffusion_paths[i, :])
    plt.title("Merton's Jump Diffusion Model")
    plt.xlabel("Time to Maturity")
    plt.ylabel("Stock Price")
    plt.show()

if __name__ == "__main__":
    main()
