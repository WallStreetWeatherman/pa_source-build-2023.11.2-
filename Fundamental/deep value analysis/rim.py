# Residual Income Model Analysis
# ------------------------------
# Overview:
# The Residual Income Model estimates a company's intrinsic value by subtracting the equity charge 
# (equity capital multiplied by the cost of equity) from the net income of a company.
# It provides a measure of how much money a company is making above and beyond its cost of equity capital.
# This model is especially valuable for assessing companies that reinvest a large portion of their earnings.
# 
# Formula:
# Residual Income = Net Income - (Equity Capital * Cost of Equity)
# 
# Desired Value:
# A positive and growing Residual Income suggests the company is generating more income than required 
# to compensate equity investors, indicating value creation.

class Company:
    def __init__(self, name, net_income, equity_capital, cost_of_equity):
        self.name = name
        self.net_income = net_income  # Format: 1.00 means $1 million
        self.equity_capital = equity_capital
        self.cost_of_equity = cost_of_equity

        # Validate data upon initialization
        self._validate_data()

    def _validate_data(self):
        """Validate data to ensure appropriate values."""
        if self.net_income <= 0:
            raise ValueError("Net Income must be positive.")
        if self.equity_capital <= 0:
            raise ValueError("Equity Capital must be positive.")
        if not (0 <= self.cost_of_equity <= 1):
            raise ValueError("Cost of Equity should be between 0 and 1 (0% to 100%).")

    def compute_residual_income(self):
        """Compute the Residual Income."""
        equity_charge = self.equity_capital * self.cost_of_equity
        return self.net_income - equity_charge

    def display_residual_income(self):
        try:
            result = self.compute_residual_income()
            print(f"Residual Income for {self.name}: {result:.2f} (in millions)")
        except Exception as e:
            print(f"An error occurred while processing data for {self.name}. Error: {str(e)}")

# Hardcoded values for two hypothetical companies
company_A = Company("Company A", 12.00, 50.00, 0.08)  # Sample data for Company A
company_A.display_residual_income()

company_B = Company("Company B", 20.00, 80.00, 0.07)  # Sample data for Company B
company_B.display_residual_income()
