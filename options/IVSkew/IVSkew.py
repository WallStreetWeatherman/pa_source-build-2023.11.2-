import matplotlib.pyplot as plt

def plot_iv_skew(strike_prices, implied_volatilities):
    """Plot the implied volatility skew."""
    plt.figure(figsize=(10,6))
    plt.plot(strike_prices, implied_volatilities, 'o-', label="IV Skew")
    plt.title("Implied Volatility Skew")
    plt.xlabel("Strike Price")
    plt.ylabel("Implied Volatility")
    plt.grid(True)
    plt.legend()
    plt.show()

def main():
    # Hard-coded values as an example
    strike_prices = [90, 95, 100, 105, 110]
    implied_volatilities = [0.22, 0.21, 0.20, 0.21, 0.22]

    plot_iv_skew(strike_prices, implied_volatilities)

if __name__ == "__main__":
    main()
