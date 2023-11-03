class Company:
    def __init__(self, name, nopat, capital, wacc):
        self.name = name
        
        # Multiply values by 1,000,000 for internal computations
        self.nopat = nopat * 1_000_000
        self.capital = capital * 1_000_000
        self.wacc = wacc
        
        # Validate the data upon initialization
        self._validate_data()

    def _validate_data(self):
        """Validate data to ensure positive capital and valid WACC."""
        if self.capital <= 0:
            raise ValueError("Capital must be positive.")
        
        if not (0 <= self.wacc <= 1):
            raise ValueError("WACC should be between 0 and 1 (0% to 100%).")

    def economic_value_added(self):
        """Compute the EVA."""
        return self.nopat - (self.capital * self.wacc)

def display_eva(company):
    try:
        eva = company.economic_value_added()
        status = "Positive EVA (creation of value)" if eva > 0 else "Negative EVA (not generating a return above its cost of capital)"
        print(f"Economic Value Added for {company.name}: {eva:.2f}")
        print(status + "\n")
    except Exception as e:
        print(f"An error occurred while processing the data for {company.name}. Error: {str(e)}\n")

# Hardcoded values in decimals representing millions
company_A = Company("Company A", nopat=0.05, capital=0.4, wacc=0.1)  # WACC represented as 10%
display_eva(company_A)

company_B = Company("Company B", nopat=0.03, capital=0.3, wacc=0.08)  # WACC represented as 8%
display_eva(company_B)
