import numpy as np
from sklearn.kernel_ridge import KernelRidge

# Sample data
strikes = np.array([90, 95, 100, 105, 110])
maturities = np.array([0.25, 0.5, 1.0, 1.5, 2.0])
implied_vols = np.array([[0.22, 0.2, 0.18, 0.2, 0.23], 
                         [0.21, 0.19, 0.18, 0.19, 0.21],
                         [0.2, 0.19, 0.17, 0.18, 0.2],
                         [0.2, 0.18, 0.17, 0.18, 0.2],
                         [0.21, 0.18, 0.16, 0.17, 0.19]])

# Parametric component functions
def f1(K, T):
    return K

def f2(K, T):
    return T

# Model calibration
def calibrate(alpha, beta_1, beta_2, K, T, implied_vols):
    parametric = alpha + beta_1 * f1(K, T) + beta_2 * f2(K, T)
    residuals = implied_vols - parametric
    
    kr = KernelRidge(kernel="rbf")
    X = np.column_stack([K.ravel(), T.ravel()])
    kr.fit(X, residuals.ravel())
    
    return kr

# Implied Volatility Function
def sigma(K, T, kr, alpha, beta_1, beta_2):
    parametric = alpha + beta_1 * f1(K, T) + beta_2 * f2(K, T)
    non_parametric = kr.predict(np.column_stack([K.ravel(), T.ravel()])).reshape(K.shape)
    return parametric + non_parametric

def main():
    K, T = np.meshgrid(strikes, maturities)
    
    # Initial values
    alpha = 0.18
    beta_1 = 0.01
    beta_2 = -0.02
    
    kr_model = calibrate(alpha, beta_1, beta_2, K, T, implied_vols)
    iv_preds = sigma(K, T, kr_model, alpha, beta_1, beta_2)
    
    # Print results
    for i, maturity in enumerate(maturities):
        print(f"For maturity {maturity} years:")
        for j, strike in enumerate(strikes):
            print(f"\tStrike: {strike}, Actual IV: {implied_vols[i][j]:.4f}, Predicted IV: {iv_preds[i][j]:.4f}")
        print("\n")

if __name__ == "__main__":
    main()