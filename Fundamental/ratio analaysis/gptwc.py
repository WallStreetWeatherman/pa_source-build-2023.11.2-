#gross profit to working capital ratio

class Company:
    def __init__(self, name, current_assets, current_liabilities, gross_profit):
        self.name = name
        self.current_assets = current_assets  # Represented in millions (e.g., 15.00 is $15 million)
        self.current_liabilities = current_liabilities  # Represented in millions
        self.gross_profit = gross_profit  # Represented in millions

        # Validate the data upon initialization
        self._validate_data()

    def _validate_data(self):
        """Validate data to ensure positive values."""
        if any(val <= 0 for val in [self.current_assets, self.current_liabilities, self.gross_profit]):
            raise ValueError("All financial values should be positive.")

    @property
    def working_capital(self):
        """Calculate the working capital."""
        return self.current_assets - self.current_liabilities

    def gp_to_wc_ratio(self):
        """Calculate the Gross Profit to Working Capital Ratio."""
        if self.working_capital == 0:
            raise ValueError("Working Capital is zero, GP to WC ratio is undefined.")
        return self.gross_profit / self.working_capital

    def display_ratio(self):
        try:
            ratio = self.gp_to_wc_ratio()
            print(f"Gross Profit to Working Capital Ratio for {self.name}: {ratio:.2f} (where a value of 1.00 represents $1 million)\n")
        except Exception as e:
            print(f"An error occurred while processing the data for {self.name}. Error: {str(e)}\n")

# Hardcoded values for two hypothetical companies
# For instance, 15.00 represents $15 million
company_A = Company(name="Company A", current_assets=15.00, current_liabilities=5.00, gross_profit=8.00)
company_A.display_ratio()

company_B = Company(name="Company B", current_assets=30.00, current_liabilities=20.00, gross_profit=10.00)
company_B.display_ratio()
