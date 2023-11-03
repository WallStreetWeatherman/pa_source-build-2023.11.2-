import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.optimize import minimize

# Heston call price using Fourier transform
def heston_call_price(kappa, theta, sigma, rho, v0, r, T, S0, K):
    def d(u):
        return np.sqrt((rho * sigma * 1j * u - kappa)**2 + sigma**2 * (1j * u + u**2))

    def g(u):
        num = kappa - rho * sigma * 1j * u - d(u)
        den = kappa - rho * sigma * 1j * u + d(u)
        return num / den

    def C(u):
        val1 = r * T * 1j * u + (1 - np.exp(-d(u) * T)) / (1 - g(u) * np.exp(-d(u) * T))
        val2 = (kappa * theta) / (sigma**2)
        return r * 1j * u * T + val1 * val2

    def D(u):
        val1 = 1 - np.exp(-d(u) * T)
        val2 = 1 - g(u) * np.exp(-d(u) * T)
        return (val1 / val2) * (kappa - rho * sigma * 1j * u - d(u))

    def integrand(u):
        return np.exp(C(u) + D(u) * v0 + 1j * u * np.log(S0 / K)) / (1j * u)

    integral = quad(lambda u: np.real(integrand(u)), 0, np.inf)[0]
    return 0.5 + (1 / np.pi) * integral

def objective(params, *args):
    kappa, theta, sigma, rho, v0 = params
    r, T, market_data = args

    total_error = 0
    for S0, K, market_price in market_data:
        model_price = heston_call_price(kappa, theta, sigma, rho, v0, r, T, S0, K)
        total_error += (model_price - market_price)**2

    return total_error

def calibrate_to_market_data(market_data, r, T, init_params):
    result = minimize(objective, init_params, args=(r, T, market_data), bounds=[(0.1, 5), (0.01, 0.1), (0.1, 1), (-0.99, 0.99), (0.01, 0.1)])
    return result.x if result.success else None

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

    # For calibration, use market data in the form: [(S0, K, market_price), ...]
    market_data = [(100, 110, 12), (100, 105, 14), (100, 115, 10)]  # Example data
    init_params = [kappa, theta, sigma, rho, v0]
    r = mu  # risk-free rate
    calibrated_params = calibrate_to_market_data(market_data, r, T, init_params)
    print("Calibrated Parameters:", calibrated_params)

    # Plot simulations
    plt.figure(figsize=(10, 6))
    for i in range(num_simulations):
        plt.plot(np.linspace(0, T, int(T / dt)), stock_paths[i, :])
    plt.title('Heston Model Stock Price Paths')
    plt.xlabel('Time to Maturity')
    plt.ylabel('Stock Price')
    plt.show()

if __name__ == "__main__":
    main()