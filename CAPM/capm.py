class Asset:
    def __init__(self, name, beta, risk_free_rate, expected_market_return):
        self.name = name
        self.beta = beta
        self.risk_free_rate = risk_free_rate
        self.expected_market_return = expected_market_return
        
        # Validate the data upon initialization
        self._validate_data()

    def _validate_data(self):
        """Validate data to ensure no negative beta and valid rates."""
        if self.beta < 0:
            raise ValueError("Beta must be non-negative.")
        
        if not (0 <= self.risk_free_rate <= 1) or not (0 <= self.expected_market_return <= 1):
            raise ValueError("Risk-free rate and expected market return should be between 0 and 1 (0% to 100%).")

    def expected_return(self):
        """Compute the expected return using the CAPM formula."""
        return self.risk_free_rate + self.beta * (self.expected_market_return - self.risk_free_rate)

def display_expected_return(asset):
    try:
        print(f"Expected Return for {asset.name}: {asset.expected_return():.2f}\n")
    except Exception as e:
        print(f"An error occurred while processing the data for {asset.name}. Error: {str(e)}\n")

# Hardcoded values for two hypothetical assets
# Values are in proportions (e.g., 0.05 represents 5%)
asset_A = Asset("Asset A", beta=1.2, risk_free_rate=0.03, expected_market_return=0.08)
display_expected_return(asset_A)

asset_B = Asset("Asset B", beta=0.8, risk_free_rate=0.03, expected_market_return=0.08)
display_expected_return(asset_B)
