# Operating Margin Calculator
# ---------------------------
# Overview:
# This script calculates the operating margin of a company, which measures how much of 
# every dollar of revenue is left over after considering both the costs of goods sold (COGS) 
# and operating expenses. It provides insights into the core profitability of a business 
# from its primary operations.
#
# Desired Value:
# A higher operating margin is typically more desirable because it indicates that the company 
# is earning more per dollar of sales and has better control over its costs. However, very high 
# margins can indicate a lack of investment or potential vulnerability to price competitions.
#
# Note: This script uses hard-coded values for demonstration. For real-world applications,
# actual financial data for the respective company should be inputted.

class OperatingMarginCalculator:
    def __init__(self, revenue, cogs, operating_expenses):
        # Convert financial values from millions representation to actual values
        # For instance, 1.00 means 1 million dollars or $1,000,000
        self.revenue = revenue * 10**6
        self.cogs = cogs * 10**6
        self.operating_expenses = operating_expenses * 10**6

    def calculate_operating_margin(self):
        """Calculate and return the operating margin."""
        if self.revenue == 0:
            return 0
        return ((self.revenue - self.cogs - self.operating_expenses) / self.revenue) * 100

    def display_operating_margin(self):
        """Display the operating margin percentage."""
        margin = self.calculate_operating_margin()
        print(f"Operating Margin is: {margin:.2f}%")

# Hard-coded values
sample_revenue = 20.00  # Example: $20 million in revenue
sample_cogs = 8.00  # Example: $8 million as the cost of goods sold
sample_operating_expenses = 4.00  # Example: $4 million in operating expenses

margin_calculator = OperatingMarginCalculator(sample_revenue, sample_cogs, sample_operating_expenses)
margin_calculator.display_operating_margin()
