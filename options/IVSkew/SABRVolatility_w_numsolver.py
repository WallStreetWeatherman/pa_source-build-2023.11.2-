import math
from scipy.optimize import minimize

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

def calibration_error(params, *args):
    F, T, market_strikes, market_vols = args
    alpha, beta, rho, nu = params
    error = 0.0
    for K, market_vol in zip(market_strikes, market_vols):
        model_vol = sabr_volatility(F, K, T, alpha, beta, rho, nu)
        error += (model_vol - market_vol)**2  # Sum of squared errors
    return error

def calibrate_sabr(F, T, market_strikes, market_vols):
    # Initial guesses for SABR parameters
    initial_params = [0.2, 0.7, 0.0, 0.1]  # [alpha, beta, rho, nu]
    
    # Constraints for parameters
    bounds = [(0.001, 2), (0, 1), (-0.999, 0.999), (0.001, 2)]
    
    result = minimize(calibration_error, initial_params, args=(F, T, market_strikes, market_vols), bounds=bounds)
    
    if result.success:
        calibrated_alpha, calibrated_beta, calibrated_rho, calibrated_nu = result.x
        return calibrated_alpha, calibrated_beta, calibrated_rho, calibrated_nu
    else:
        raise ValueError("Calibration did not converge!")

def main():
    # Market data: Strikes and corresponding market implied volatilities
    market_strikes = [90, 100, 110]
    market_vols = [0.2, 0.18, 0.19]
    
    # forward price and time to expiration
    F = 100
    T = 1.0
    
    alpha, beta, rho, nu = calibrate_sabr(F, T, market_strikes, market_vols)
    
    print(f"Calibrated Parameters:\nAlpha={alpha:.4f}\nBeta={beta:.4f}\nRho={rho:.4f}\nNu={nu:.4f}")

if __name__ == "__main__":
    main()