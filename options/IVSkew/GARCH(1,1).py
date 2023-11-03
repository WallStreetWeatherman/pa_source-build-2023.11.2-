import numpy as np
import matplotlib.pyplot as plt
from arch import arch_model

def simulate_garch(mu, alpha0, alpha1, beta1, num_days, z0, sigma0):
    # Initialize arrays
    returns = np.zeros(num_days)
    sigma = np.zeros(num_days)
    epsilon = np.zeros(num_days)
    
    sigma[0] = sigma0
    epsilon[0] = z0 * sigma[0]
    returns[0] = mu + epsilon[0]
    
    for t in range(1, num_days):
        sigma[t] = np.sqrt(alpha0 + alpha1 * epsilon[t-1]**2 + beta1 * sigma[t-1]**2)
        epsilon[t] = sigma[t] * np.random.normal(0, 1)
        returns[t] = mu + epsilon[t]
        
    return returns, sigma

def main():
    # GARCH(1,1) Parameters
    mu = 0.0
    alpha0 = 0.1
    alpha1 = 0.3
    beta1 = 0.6
    num_days = 1000
    z0 = np.random.normal(0, 1)
    sigma0 = np.sqrt(alpha0 / (1 - alpha1 - beta1))
    
    # Simulate GARCH(1,1) returns and volatility
    returns, sigma = simulate_garch(mu, alpha0, alpha1, beta1, num_days, z0, sigma0)
    
    # Fit a GARCH(1,1) model to our simulated returns
    model = arch_model(returns, vol='Garch', p=1, q=1)
    results = model.fit(update_freq=5)
    print(results.summary())
    
    # Plot the simulated returns and volatility
    fig, ax = plt.subplots(2, 1, figsize=(10, 6))
    ax[0].plot(returns)
    ax[0].set_title('Simulated GARCH(1,1) Returns')
    ax[1].plot(sigma)
    ax[1].set_title('Simulated GARCH(1,1) Volatility')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
