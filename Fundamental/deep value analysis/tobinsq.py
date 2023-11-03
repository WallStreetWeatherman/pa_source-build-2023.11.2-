# Q-Ratio (Tobin's Q) Analysis
# ----------------------------
# Overview:
# The Q-Ratio (often referred to as Tobin's Q) is a metric used to determine the valuation
# of a company's assets. It is the ratio of the market value of a company's assets to 
# their replacement value. 
#
# Formula:
# Q-Ratio = Market Value of Assets / Replacement Value of Assets
# 
# Desired Value:
# A Q-ratio below 1 can suggest that a company's stock is undervalued. However, be wary
# that extremely low Q-Ratios may also indicate distressed companies or those in declining industries.

class Company:
    def __init__(self, name, market_value_of_assets, replacement_value_of_assets):
        self.name = name
        self.market_value_of_assets = market_value_of_assets  # Format: 1.00 means $1 million
        self.replacement_value_of_assets = replacement_value_of_assets

        # Validate data upon initialization
        self._validate_data()

    def _validate_data(self):
        """Validate data to ensure appropriate values."""
        if any(value < 0 for value in [self.market_value_of_assets, self.replacement_value_of_assets]):
            raise ValueError("Values must be non-negative.")

    def compute_q_ratio(self):
        """Compute the Q-Ratio."""
        return self.market_value_of_assets / self.replacement_value_of_assets

    def is_undervalued(self):
        """Determine if the company's assets are potentially undervalued based on Q-Ratio."""
        return self.compute_q_ratio() < 1

    def display_q_ratio(self):
        try:
            result = self.compute_q_ratio()
            status = "Undervalued" if self.is_undervalued() else "Not Undervalued"
            print(f"Q-Ratio for {self.name}: {result:.2f}. Status: {status}.")
        except Exception as e:
            print(f"An error occurred while processing data for {self.name}. Error: {str(e)}")

# Hardcoded values for two hypothetical companies
company_A = Company("Company A", 10.00, 12.00)  # Sample data for Company A
company_A.display_q_ratio()

company_B = Company("Company B", 25.00, 20.00)  # Sample data for Company B
company_B.display_q_ratio()
