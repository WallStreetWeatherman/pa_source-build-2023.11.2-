# PEG Ratio (Price/Earnings to Growth) Calculator

class Company:
    def __init__(self, name, current_stock_price, earnings_per_share, expected_eps_growth_rate):
        self.name = name
        self.current_stock_price = current_stock_price  # in millions
        self.earnings_per_share = earnings_per_share  # Earnings Per Share (EPS) in millions
        self.expected_eps_growth_rate = expected_eps_growth_rate  # Expected annual growth rate in EPS (as a percentage, so 0.10 represents 10%)

        # Validate the data upon initialization
        self._validate_data()

    def _validate_data(self):
        """Validate data to ensure positive values."""
        if any(val <= 0 for val in [self.current_stock_price, self.earnings_per_share]):
            raise ValueError("Stock price and EPS should be positive.")
        if not (0 <= self.expected_eps_growth_rate <= 1):
            raise ValueError("Expected EPS Growth Rate should be between 0 and 1 (0% to 100%).")

    def pe_ratio(self):
        return self.current_stock_price / self.earnings_per_share

    def peg_ratio(self):
        return self.pe_ratio() / self.expected_eps_growth_rate

    def display_peg_ratio(self):
        try:
            peg = self.peg_ratio()
            status = "Potentially undervalued" if peg < 1 else "Not necessarily undervalued"
            print(f"PEG Ratio for {self.name}: {peg:.2f}")
            print(status + "\n")
        except Exception as e:
            print(f"An error occurred while processing the data for {self.name}. Error: {str(e)}\n")

# Hardcoded values for two hypothetical companies
company_A = Company(name="Company A", current_stock_price=100.00, earnings_per_share=5.00, expected_eps_growth_rate=0.12)  # 12% expected growth rate
company_A.display_peg_ratio()

company_B = Company(name="Company B", current_stock_price=150.00, earnings_per_share=7.00, expected_eps_growth_rate=0.10)  # 10% expected growth rate
company_B.display_peg_ratio()
