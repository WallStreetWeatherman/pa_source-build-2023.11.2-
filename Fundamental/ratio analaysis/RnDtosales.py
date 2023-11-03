# R&D to Sales Ratio Calculator

class Company:
    def __init__(self, name, rd_expenses, total_sales):
        self.name = name
        self.rd_expenses = rd_expenses  # R&D Expenses in millions
        self.total_sales = total_sales  # Total Sales in millions
        
        # Validate the data upon initialization
        self._validate_data()

    def _validate_data(self):
        """Validate data to ensure positive values."""
        if any(val <= 0 for val in [self.rd_expenses, self.total_sales]):
            raise ValueError("R&D Expenses and Total Sales should be positive.")

    def rd_to_sales_ratio(self):
        return self.rd_expenses / self.total_sales

    def display_rd_to_sales_ratio(self):
        try:
            ratio = self.rd_to_sales_ratio()
            print(f"R&D to Sales Ratio for {self.name}: {ratio:.2f}\n")
        except Exception as e:
            print(f"An error occurred while processing the data for {self.name}. Error: {str(e)}\n")

# Hardcoded values for two hypothetical companies
company_A = Company(name="Company A", rd_expenses=50.00, total_sales=500.00)  # Representing $50 million R&D and $500 million sales
company_A.display_rd_to_sales_ratio()

company_B = Company(name="Company B", rd_expenses=30.00, total_sales=250.00)  # Representing $30 million R&D and $250 million sales
company_B.display_rd_to_sales_ratio()
