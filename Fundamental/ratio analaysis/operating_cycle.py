class Company:
    def __init__(self, name, inventory, cost_of_goods_sold_annual, accounts_receivable, sales_annual):
        self.name = name
        self.inventory = inventory  # Represented in millions, e.g., 1.00 is $1 million
        self.cost_of_goods_sold_annual = cost_of_goods_sold_annual  # Annual COGS in millions
        self.accounts_receivable = accounts_receivable  # Represented in millions
        self.sales_annual = sales_annual  # Annual Sales in millions

        # Validate the data upon initialization
        self._validate_data()

    def _validate_data(self):
        """Validate data to ensure positive values."""
        if any(val <= 0 for val in [self.inventory, self.cost_of_goods_sold_annual, self.accounts_receivable, self.sales_annual]):
            raise ValueError("All financial values should be positive.")

    def days_sales_of_inventory(self):
        """Calculate Days Sales of Inventory."""
        cogs_per_day = self.cost_of_goods_sold_annual / 365
        return self.inventory / cogs_per_day

    def days_sales_outstanding(self):
        """Calculate Days Sales Outstanding."""
        sales_per_day = self.sales_annual / 365
        return self.accounts_receivable / sales_per_day

    def operating_cycle(self):
        """Calculate the Operating Cycle in days."""
        return self.days_sales_of_inventory() + self.days_sales_outstanding()

    def display_operating_cycle(self):
        try:
            print(f"Operating Cycle for {self.name}: {self.operating_cycle():.2f} days\n")
        except Exception as e:
            print(f"An error occurred while processing the data for {self.name}. Error: {str(e)}\n")

# Hardcoded values for two hypothetical companies
# For instance, 2.00 in inventory represents $2 million worth of inventory
company_A = Company(name="Company A", inventory=2.00, cost_of_goods_sold_annual=10.00, accounts_receivable=1.50, sales_annual=12.00)
company_A.display_operating_cycle()

company_B = Company(name="Company B", inventory=1.50, cost_of_goods_sold_annual=8.00, accounts_receivable=1.00, sales_annual=10.00)
company_B.display_operating_cycle()
