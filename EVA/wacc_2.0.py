class Company:
    def __init__(self, name, market_value_of_equity, market_value_of_debt, cost_of_equity, cost_of_debt, tax_rate):
        self.name = name
        
        # Multiply values by 1,000,000 for internal computations
        self.market_value_of_equity = market_value_of_equity * 1_000_000
        self.market_value_of_debt = market_value_of_debt * 1_000_000
        self.cost_of_equity = cost_of_equity
        self.cost_of_debt = cost_of_debt
        self.tax_rate = tax_rate
        
        # Validate the data upon initialization
        self._validate_data()

    def _validate_data(self):
        """Validate data to ensure positive values and valid rates."""
        if any(val <= 0 for val in [self.market_value_of_equity, self.market_value_of_debt, self.cost_of_equity, self.cost_of_debt]):
            raise ValueError("Equity, Debt, Cost of Equity, and Cost of Debt values must be positive.")
        
        if not (0 <= self.tax_rate <= 1):
            raise ValueError("Tax Rate should be between 0 and 1 (0% to 100%).")

    def wacc(self):
        """Compute the WACC."""
        V = self.market_value_of_equity + self.market_value_of_debt
        equity_weight = self.market_value_of_equity / V
        debt_weight = self.market_value_of_debt / V
        return equity_weight * self.cost_of_equity + debt_weight * self.cost_of_debt * (1 - self.tax_rate)

def display_wacc(company):
    try:
        print(f"Weighted Average Cost of Capital (WACC) for {company.name}: {company.wacc():.2f}\n")
    except Exception as e:
        print(f"An error occurred while processing the data for {company.name}. Error: {str(e)}\n")

# Hardcoded values in decimals representing millions
company_A = Company("Company A", 0.5, 0.3, 0.08, 0.05, 0.3)  # Rates represented as 8%, 5%, and 30% respectively
display_wacc(company_A)

company_B = Company("Company B", 0.6, 0.4, 0.07, 0.06, 0.25)  # Rates represented as 7%, 6%, and 25% respectively
display_wacc(company_B)
