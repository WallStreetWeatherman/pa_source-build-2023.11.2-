class Company:
    def __init__(self, name, operating_profit, tax_rate):
        self.name = name
        
        # Multiply values by 1,000,000 for internal computations
        self.operating_profit = operating_profit * 1_000_000
        self.tax_rate = tax_rate
        
        # Validate the data upon initialization
        self._validate_data()

    def _validate_data(self):
        """Validate data to ensure positive operating profit and valid tax rate."""
        if self.operating_profit <= 0:
            raise ValueError("Operating Profit must be positive.")
        
        if not (0 <= self.tax_rate <= 1):
            raise ValueError("Tax Rate should be between 0 and 1 (0% to 100%).")

    def nopat(self):
        """Compute the NOPAT."""
        return self.operating_profit * (1 - self.tax_rate)

def display_nopat(company):
    try:
        print(f"Net Operating Profit After Taxes (NOPAT) for {company.name}: {company.nopat():.2f}\n")
    except Exception as e:
        print(f"An error occurred while processing the data for {company.name}. Error: {str(e)}\n")

# Hardcoded values in decimals representing millions
company_A = Company("Company A", operating_profit=0.15, tax_rate=0.3)  # Tax rate represented as 30%
display_nopat(company_A)

company_B = Company("Company B", operating_profit=0.1, tax_rate=0.25)  # Tax rate represented as 25%
display_nopat(company_B)
