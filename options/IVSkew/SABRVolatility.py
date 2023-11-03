import math

def sabr_volatility(F, K, T, alpha, beta, rho, nu):
    """Calculate the SABR implied volatility with real-world considerations."""

    if F == K:
        # Handle the ATM case
        vol_atm = alpha / (F**(1-beta)) * (1 + ((1-beta)**2/24 * (math.log(F/K))**2 + ((1-beta)**4)/1920 * (math.log(F/K))**4) * T)
        return vol_atm
    
    else:
        # Calculate z and x values
        z = nu/alpha * (F*K)**((1-beta)/2) * math.log(F/K)
        x = math.log((math.sqrt(1 - 2*rho*z + z**2) + z - rho) / (1 - rho))
        
        # Return the SABR implied volatility
        return (nu * (F*K)**((1-beta)/2) * z) / (x * (1 + ((1-beta)**2/24) * math.log(F/K)**2 + (((1-beta)*rho*nu*alpha)/4) * (F*K)**((1-beta)/2) * math.log(F/K) + (nu**2/24 + (2-3*rho**2)/24) * T))

def main():
    # Hard-coded values
    F = 100.0          # Forward rate
    K = 110.0          # Strike price
    T = 1.0            # Time to expiration in years
    alpha = 0.2        # Volatility level parameter
    beta = 0.5         # Price process parameter (0 <= beta <= 1)
    rho = -0.4         # Correlation parameter (-1 <= rho <= 1)
    nu = 0.5           # Volatility of volatility parameter
    
    implied_vol = sabr_volatility(F, K, T, alpha, beta, rho, nu)
    
    print(f"The SABR implied volatility is: {implied_vol:.2f}")

if __name__ == "__main__":
    main()
