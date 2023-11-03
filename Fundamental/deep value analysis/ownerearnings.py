# Owner Earnings Analysis
# -----------------------
# Overview:
# Owner Earnings, as popularized by Warren Buffett, represent the true profitability of a company. 
# It is the cash flow that could be theoretically distributed to shareholders, after all operating expenses, 
# taxes, and reinvestment needs are covered. It’s considered a more realistic view of a company's real earning power.
# For a deep value investor, a growing trend in Owner Earnings over time suggests that the company's profitability 
# and intrinsic value are increasing.
# 
# Formula:
# Owner Earnings = Net Income + Depreciation & Amortization - CapEx - Changes in Working Capital

class Company:
    def __init__(self, name, net_income, depreciation_amortization, capex, change_in_working_capital):
        self.name = name
        self.net_income = net_income  # In format: 1.00 means $1 million
        self.depreciation_amortization = depreciation_amortization
        self.capex = capex
        self.change_in_working_capital = change_in_working_capital

        # Validate the data upon initialization
        self._validate_data()

    def _validate_data(self):
        """Validate data to ensure appropriate values."""
        if self.net_income <= 0:
            raise ValueError("Net Income must be positive.")
        if self.depreciation_amortization < 0:
            raise ValueError("Depreciation & Amortization cannot be negative.")
        if self.capex < 0:
            raise ValueError("CapEx cannot be negative.")
        # No validation for change_in_working_capital as it can be negative

    def compute_owner_earnings(self):
        """Compute the Owner Earnings."""
        return self.net_income + self.depreciation_amortization - self.capex - self.change_in_working_capital

    def display_owner_earnings(self):
        try:
            print(f"Owner Earnings for {self.name}: {self.compute_owner_earnings():.2f} (in millions)")
        except Exception as e:
            print(f"An error occurred while processing the data for {self.name}. Error: {str(e)}")

# Hardcoded values for two hypothetical companies
company_A = Company("Company A", 12.00, 3.00, 2.50, 1.00)  # Sample data for Company A
company_A.display_owner_earnings()

company_B = Company("Company B", 20.00, 4.50, 3.00, 2.00)  # Sample data for Company B
company_B.display_owner_earnings()
