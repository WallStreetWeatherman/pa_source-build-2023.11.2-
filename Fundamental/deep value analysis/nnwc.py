# Net-Net Working Capital (NNWC) Analysis
# ---------------------------------------
# Overview:
# The Net-Net Working Capital (NNWC) is a concept popularized by Benjamin Graham.
# A company might be considered undervalued if its market capitalization is less than its NNWC.
# 
# Formula:
# NNWC = Current Assets - Total Liabilities - Preferred Stock
# 
# Desired Value:
# If NNWC is greater than the market capitalization, it could be an indication that the stock 
# is significantly undervalued. However, this is a conservative approach, and other factors 
# should also be considered in a comprehensive analysis.

class Company:
    def __init__(self, name, current_assets, total_liabilities, preferred_stock, market_cap):
        self.name = name
        self.current_assets = current_assets  # Format: 1.00 means $1 million
        self.total_liabilities = total_liabilities
        self.preferred_stock = preferred_stock
        self.market_cap = market_cap

        # Validate data upon initialization
        self._validate_data()

    def _validate_data(self):
        """Validate data to ensure appropriate values."""
        if any(value < 0 for value in [self.current_assets, self.total_liabilities, self.preferred_stock, self.market_cap]):
            raise ValueError("Values must be non-negative.")

    def compute_nnwc(self):
        """Compute the Net-Net Working Capital."""
        return self.current_assets - self.total_liabilities - self.preferred_stock

    def is_undervalued(self):
        """Determine if the company is potentially undervalued based on NNWC."""
        return self.compute_nnwc() > self.market_cap

    def display_nnwc(self):
        try:
            result = self.compute_nnwc()
            status = "Undervalued" if self.is_undervalued() else "Not Undervalued"
            print(f"NNWC for {self.name}: {result:.2f} (in millions). Status: {status}.")
        except Exception as e:
            print(f"An error occurred while processing data for {self.name}. Error: {str(e)}")

# Hardcoded values for two hypothetical companies
company_A = Company("Company A", 10.00, 3.00, 1.00, 5.00)  # Sample data for Company A
company_A.display_nnwc()

company_B = Company("Company B", 25.00, 15.00, 2.00, 8.00)  # Sample data for Company B
company_B.display_nnwc()
