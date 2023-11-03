# Capital Expenditure (CapEx) as % of Sales Calculator
# ----------------------------------------------------
# Overview:
# Capital Expenditure (CapEx) is the funds used by a company to acquire, maintain, and 
# upgrade fixed assets. When you calculate CapEx as a percentage of sales, it gives insights 
# into how much of its revenue a company is reinvesting in its core operations and growth.
#
# Desired Value:
# Whether a higher or lower percentage is desired depends on the specific industry and 
# the growth phase of the company. Newer or expanding companies may have a higher CapEx 
# as a percentage of sales because they're investing in growth. Mature companies might have 
# a lower percentage as they've already built out their necessary infrastructure.
#
# Note: This script uses hard-coded values for demonstration. For real-world applications,
# actual sales data and CapEx data should be inputted.

class CapExPercentageCalculator:
    def __init__(self, sales, capex):
        # Convert sales and capex from millions representation to actual values
        # For instance, 1.00 means 1 million dollars or $1,000,000
        self.sales = sales * 10**6
        self.capex = capex * 10**6

    def calculate_capex_percentage(self):
        """Calculate and return the CapEx as a percentage of Sales."""
        return (self.capex / self.sales) * 100 if self.sales != 0 else 0

    def display_capex_percentage(self):
        """Display the CapEx as a percentage of Sales."""
        capex_percentage = self.calculate_capex_percentage()
        print(f"CapEx as a percentage of Sales is: {capex_percentage:.2f}%")

# Hard-coded values
sample_sales = 50.00  # Example: Sales of $50 million
sample_capex = 10.00  # Example: CapEx of $10 million

capex_calculator = CapExPercentageCalculator(sample_sales, sample_capex)
capex_calculator.display_capex_percentage()

