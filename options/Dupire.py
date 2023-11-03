import numpy as np
from scipy.interpolate import interp2d

# Sample market implied volatilities (this is just illustrative data)
STRIKES = [90, 100, 110]
MATURITIES = [0.5, 1.0, 1.5]
IMPLIED_VOLS = [
    [0.18, 0.15, 0.17],
    [0.19, 0.16, 0.18],
    [0.20, 0.17, 0.19]
]

# Use cubic spline interpolation to get a smoother implied volatility surface
ivol_surface = interp2d(STRIKES, MATURITIES, IMPLIED_VOLS, kind='cubic')

def implied_volatility(S, T):
    return ivol_surface(S, T)[0]

# Calculate local volatility using Dupire's formula with finite differences
def local_volatility(S, T, h=1.0):
    # Numerical derivatives
    dV_dT = (implied_volatility(S, T + h) - implied_volatility(S, T - h)) / (2 * h)
    dV_dS = (implied_volatility(S + h, T) - implied_volatility(S - h, T)) / (2 * h)
    d2V_dS2 = (implied_volatility(S + h, T) - 2 * implied_volatility(S, T) + implied_volatility(S - h, T)) / h**2

    # Dupire's formula
    numerator = dV_dT + 0.05 * S * dV_dS + 0.05 * implied_volatility(S, T)**2
    denominator = 0.5 * S**2 * d2V_dS2

    if denominator <= 0:
        return implied_volatility(S, T)

    return np.sqrt(2 * numerator / denominator)

def main():
    # Example: Compute local volatility for a stock price of 105 and time of 0.5 years
    S = 105
    T = 0.5
    print(f"Local Volatility at S={S} and T={T} is: {local_volatility(S, T):.4f}")

if __name__ == "__main__":
    main()