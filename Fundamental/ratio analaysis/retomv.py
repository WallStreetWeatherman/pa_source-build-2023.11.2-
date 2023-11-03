# Retained Earnings to Market Value Ratio Calculator

class Company:
    def __init__(self, name, retained_earnings, market_value):
        self.name = name
        self.retained_earnings = retained_earnings  # Retained Earnings in millions
        self.market_value = market_value  # Market Value in millions
        
        # Validate the data upon initialization
        self._validate_data()

    def _validate_data(self):
        """Validate data to ensure positive values."""
        if any(val <= 0 for val in [self.retained_earnings, self.market_value]):
            raise ValueError("Both Retained Earnings and Market Value should be positive values.")

    def retained_earnings_to_market_value_ratio(self):
        return self.retained_earnings / self.market_value

    def display_ratio(self):
        try:
            ratio = self.retained_earnings_to_market_value_ratio()
            print(f"Retained Earnings to Market Value Ratio for {self.name}: {ratio:.2f}\n")
        except Exception as e:
            print(f"An error occurred while processing the data for {self.name}. Error: {str(e)}\n")

# Hardcoded values for two hypothetical companies
company_A = Company(name="Company A", retained_earnings=150.00, market_value=1000.00)  # Representing $150 million retained earnings and $1 billion market value
company_A.display_ratio()

company_B = Company(name="Company B", retained_earnings=80.00, market_value=500.00)  # Representing $80 million retained earnings and $500 million market value
company_B.display_ratio()
