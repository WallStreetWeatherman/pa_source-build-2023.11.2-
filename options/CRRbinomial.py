import math

def american_binomial(S, K, r, v, T, n, option_type='call', div_yield=0.0):
    """
    Calculate the American option price with the Binomial Model.
    S: Current stock price
    K: Option strike price
    r: Risk-free rate (annual)
    v: Volatility (annual)
    T: Time to expiration (in years)
    n: Number of binomial steps
    option_type: 'call' or 'put'
    div_yield: Dividend yield (annual)
    """
    
    dt = T/n  # Time step
    discount = math.exp(-r * dt)
    
    # Calculate the up and down price movements
    u = math.exp(v * math.sqrt(dt))
    d = 1/u
    q = (math.exp((r - div_yield) * dt) - d) / (u - d)  # Risk-neutral probability

    # Initialize the matrix to store stock prices and option prices
    stock_price = [[0 for _ in range(n+1)] for _ in range(n+1)]
    option_price = [[0 for _ in range(n+1)] for _ in range(n+1)]
    
    # Stock price tree initialization
    for j in range(n+1):
        stock_price[j][n] = S * (u**(n-j)) * (d**j)
        
    # Option price tree initialization
    for j in range(n+1):
        if option_type == "call":
            option_price[j][n] = max(0, stock_price[j][n] - K)
        elif option_type == "put":
            option_price[j][n] = max(0, K - stock_price[j][n])

    # Recursive calculation for option price
    for i in range(n-1, -1, -1):
        for j in range(i+1):
            if option_type == "call":
                option_price[j][i] = (
                    q * option_price[j][i + 1] + (1 - q) * option_price[j + 1][i + 1]
                ) * discount
                option_price[j][i] = max(option_price[j][i], stock_price[j][i] - K)
            elif option_type == "put":
                option_price[j][i] = (
                    q * option_price[j][i + 1] + (1 - q) * option_price[j + 1][i + 1]
                ) * discount
                option_price[j][i] = max(option_price[j][i], K - stock_price[j][i])
                
    return option_price[0][0]

# Test the function
S = 100
K = 100
r = 0.05
v = 0.2
T = 1
n = 100
div_yield = 0.03
option_type = "call"

price = american_binomial(S, K, r, v, T, n, option_type, div_yield)
print(f"The American {option_type} option price with dividends is: ${price:.2f}")
