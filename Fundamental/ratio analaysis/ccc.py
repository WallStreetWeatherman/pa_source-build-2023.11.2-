# Cash Conversion Cycle (CCC) Calculator

class Company:
    def __init__(self, name, inventory, cost_of_goods_sold_annual, accounts_receivable, sales_annual, accounts_payable):
        self.name = name
        self.inventory = inventory  # in millions
        self.cost_of_goods_sold_annual = cost_of_goods_sold_annual  # Annual COGS in millions
        self.accounts_receivable = accounts_receivable  # in millions
        self.sales_annual = sales_annual  # Annual Sales in millions
        self.accounts_payable = accounts_payable  # in millions

        # Validate the data upon initialization
        self._validate_data()

    def _validate_data(self):
        """Validate data to ensure positive values."""
        if any(val <= 0 for val in [self.inventory, self.cost_of_goods_sold_annual, self.accounts_receivable, self.sales_annual, self.accounts_payable]):
            raise ValueError("All financial values should be positive.")

    def days_sales_of_inventory(self):
        cogs_per_day = self.cost_of_goods_sold_annual / 365
        return self.inventory / cogs_per_day

    def days_sales_outstanding(self):
        sales_per_day = self.sales_annual / 365
        return self.accounts_receivable / sales_per_day

    def days_payable_outstanding(self):
        cogs_per_day = self.cost_of_goods_sold_annual / 365
        return self.accounts_payable / cogs_per_day

    def cash_conversion_cycle(self):
        return self.days_sales_of_inventory() + self.days_sales_outstanding() - self.days_payable_outstanding()

    def display_cash_conversion_cycle(self):
        try:
            print(f"Cash Conversion Cycle for {self.name}: {self.cash_conversion_cycle():.2f} days\n")
        except Exception as e:
            print(f"An error occurred while processing the data for {self.name}. Error: {str(e)}\n")

# Hardcoded values for two hypothetical companies
company_A = Company(name="Company A", inventory=2.00, cost_of_goods_sold_annual=10.00, accounts_receivable=1.50, sales_annual=12.00, accounts_payable=1.20)
company_A.display_cash_conversion_cycle()

company_B = Company(name="Company B", inventory=1.50, cost_of_goods_sold_annual=8.00, accounts_receivable=1.00, sales_annual=10.00, accounts_payable=0.90)
company_B.display_cash_conversion_cycle()
